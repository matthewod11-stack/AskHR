from __future__ import annotations

import io
import logging
import os
import pathlib
from importlib import import_module
from app.llm import chat_with_model

import requests
from fastapi import FastAPI, HTTPException, Query, Request
from fastapi.responses import JSONResponse, PlainTextResponse, StreamingResponse

from .error_utils import get_request_id, safe_response
from .paths import PathResolutionError, normalize_source_path
from .logging_setup import configure_json_logging
from .middleware import RequestIdLoggingMiddleware

# ------------------------------------------------------------------------------
# App & logging
# ------------------------------------------------------------------------------
configure_json_logging()
log = logging.getLogger("askhr")

app = FastAPI(title="AskHR Local API")
app.add_middleware(RequestIdLoggingMiddleware)

# A pragmatic CPO persona used for grounded answers (can be overridden per-request)
DEFAULT_PERSONA = (
    "You are a pragmatic, fair Chief People Officer. You answer concisely and concretely, "
    "cite relevant policy/source passages, and flag compliance or legal risks without alarmism. "
    "Use plain language, structured bullets when helpful, and suggest next steps. "
    "If sources are weak or missing, say so and recommend how to strengthen them."
)

# Directory that holds cleaned markdown (used by PDF export helper)
DATA_CLEAN_DIR = os.getenv("DATA_CLEAN_DIR", "data/clean")

# ------------------------------------------------------------------------------
# Health endpoints
# ------------------------------------------------------------------------------
@app.get("/health")
def health_root():
    return {"ok": True, "service": "askhr", "version": os.getenv("ASKHR_VERSION", "dev")}

@app.get("/health/ollama")
def health_ollama():
    """Tolerant of tag variants like ':latest', ':8b' when checking availability."""
    chat_model = os.getenv("OLLAMA_CHAT_MODEL", "llama3.1:8b")
    embed_model = os.getenv("OLLAMA_EMBED_MODEL", "nomic-embed-text")

    def _base(name: str) -> str:
        return (name or "").strip().lower().split(":")[0]

    try:
        r = requests.get("http://localhost:11434/api/tags", timeout=5)
        r.raise_for_status()
        models = r.json().get("models", [])
        names = [m.get("name", "") for m in models if isinstance(m, dict)]
        bases = {_base(n) for n in names}
        ok = (_base(chat_model) in bases) and (_base(embed_model) in bases)
        return JSONResponse(
            {"ok": ok, "models": {"chat": chat_model, "embed": embed_model}, "available": names},
            status_code=200 if ok else 424,
        )
    except Exception as e:
        return JSONResponse({"ok": False, "error": str(e)}, status_code=502)

# ------------------------------------------------------------------------------
# File endpoints (normalized serving for citations)
# ------------------------------------------------------------------------------
@app.get("/v1/file", response_class=PlainTextResponse)
def get_file(
    path: str = Query(..., description="Source-relative path (raw or clean). Anchor (#...) allowed; ignored by server."),
):
    if not path:
        raise HTTPException(status_code=400, detail="Missing 'path' query param")
    try:
        resolved, _ = normalize_source_path(path)
    except PathResolutionError as e:
        raise HTTPException(status_code=404, detail=str(e))
    try:
        return resolved.read_text(encoding="utf-8", errors="ignore")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to read file: {e}")

@app.get("/v1/file/normalized", response_class=PlainTextResponse)
def get_file_normalized(
    path: str = Query(..., description="Source-relative path (raw or clean). Anchor (#...) allowed; ignored by server."),
):
    return get_file(path)

# ------------------------------------------------------------------------------
# Ask endpoint (resilient; never 500s)
# ------------------------------------------------------------------------------
@app.get("/v1/ask")
def ask_get_hint():
    return {"hint": "Use POST /v1/ask with JSON body: {query, k?, grounded_only?, persona?}"}

@app.post("/v1/ask")
async def ask(request: Request):
    """
    Always returns 200 JSON:
    { "answer": str, "citations": list, "ungrounded": bool, "request_id": str, "error"?: str }
    """
    rid = get_request_id(dict(request.headers))
    try:
        body = await request.json()
        query = (body.get("query") or "").strip()
        if not query:
            return JSONResponse(safe_response({"answer": "", "citations": [], "error": "Missing 'query'."}, rid))

        try:
            k = int(body.get("k") or os.getenv("ASK_TOP_K", "8"))
        except Exception:
            k = 8
        grounded_only = bool(body.get("grounded_only") or False)

        # Persona: from request or default CPO persona
        persona = (body.get("persona") or "").strip() or DEFAULT_PERSONA

        # Dynamic imports (avoid hard failures if modules move)
        retriever = import_module("app.retriever")
        prompting = import_module("app.prompting_grounded")
        embeddings = import_module("app.embeddings")

        # Retrieval (support either export name)
        retrieve_fn = getattr(retriever, "retrieve_topk", None) or getattr(retriever, "retrieve_top_k", None)
        if not callable(retrieve_fn):
            raise RuntimeError("app.retriever missing retrieve_topk/retrieve_top_k")
        chunks = retrieve_fn(query=query, top_k=k)

        if grounded_only and not chunks:
            return JSONResponse(
                safe_response(
                    {"answer": "No relevant sources found for grounded-only mode.", "citations": [], "ungrounded": True},
                    rid,
                )
            )

        # Compose grounded prompt WITH persona (fixes missing-argument error)
        messages, citations = prompting.build_grounded_prompt(question=query, top_chunks=chunks, persona=persona)

        # LLM call (sync)
        answer_text = chat_with_model(messages) or ""

        return JSONResponse(
            safe_response(
                {"answer": answer_text, "citations": citations or [], "ungrounded": False if chunks else True},
                rid,
            )
        )

    except Exception as e:
        log.exception("ask_failed rid=%s", rid)
        return JSONResponse(safe_response({"answer": "", "citations": [], "error": str(e), "ungrounded": True}, rid))

# ------------------------------------------------------------------------------
# Simple PDF export (optional dependency on reportlab)
# ------------------------------------------------------------------------------
try:
    import reportlab  # type: ignore
    _HAS_REPORTLAB = True
except Exception:
    _HAS_REPORTLAB = False

def _markdown_body_for_source(source_path: str) -> str:
    texts = []
    for p in pathlib.Path(DATA_CLEAN_DIR).rglob("*.md"):
        raw = p.read_text(encoding="utf-8", errors="ignore")
        if raw.startswith("---") and f"source_path: {source_path}" in raw:
            parts = raw.split("---", 2)
            if len(parts) == 3:
                texts.append(parts[2].strip())
    return "\n\n".join(texts) if texts else ""

@app.get("/v1/export/pdf")
def export_pdf(source_path: str = Query(...)):
    if not _HAS_REPORTLAB:
        return JSONResponse({"error": "PDF export requires reportlab. Install with: pip install reportlab"}, status_code=406)
    body = _markdown_body_for_source(source_path)
    if not body:
        return JSONResponse({"error": "No cleaned content found for source"}, status_code=404)

    from reportlab.lib.pagesizes import LETTER  # type: ignore
    from reportlab.pdfgen import canvas  # type: ignore

    buf = io.BytesIO()
    c = canvas.Canvas(buf, pagesize=LETTER)
    width, height = LETTER
    x, y = 72, height - 72
    for line in body.splitlines():
        if y < 72:
            c.showPage()
            y = height - 72
        c.drawString(x, y, line[:110])
        y -= 14
    c.save()
    buf.seek(0)
    filename = pathlib.Path(source_path).with_suffix(".pdf").name
    return StreamingResponse(
        buf,
        media_type="application/pdf",
        headers={"Content-Disposition": f'attachment; filename="{filename}"'},
    )
