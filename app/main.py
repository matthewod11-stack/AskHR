"""
TODO(rewrite-debug): wire endpoint once design is finalized
TODO(metrics): add per-endpoint latency histograms once metrics backend is chosen
"""
import os, json, httpx, pathlib, uuid, traceback
from urllib.parse import quote
from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException, Query, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse, StreamingResponse, JSONResponse, PlainTextResponse
from typing import Optional
from .paths import normalize_source_path, PathResolutionError
from .config import settings
try:
    from reportlab.lib.pagesizes import LETTER
    from reportlab.pdfgen import canvas
    _HAS_REPORTLAB = True
except Exception:
    _HAS_REPORTLAB = False
import io
from collections import deque

from app.schemas import SearchRequest, SearchResponse, SearchHit, AskRequest, AskResponse
from app.retriever import search_chunks
from app.prompting import build_system_prompt, maybe_rewrite_query
from app.prompting_grounded import build_grounded_prompt
from app.logging_setup import logger

load_dotenv()

app = FastAPI(title="Ask HR (Local)")
app.add_middleware(
    CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"]
)

# Request ID middleware
@app.middleware("http")
async def add_request_id(request: Request, call_next):
    req_id = request.headers.get("X-Request-ID") or str(uuid.uuid4())
    request.state.request_id = req_id
    response = await call_next(request)
    if hasattr(response, "body") and isinstance(response.body, (bytes, str)):
        # Try to inject request_id into JSON responses
        try:
            body = response.body.decode() if isinstance(response.body, bytes) else response.body
            data = json.loads(body)
            if isinstance(data, dict):
                data["request_id"] = req_id
                response.body = json.dumps(data).encode()
        except Exception:
            pass
    return response

LLM_MODEL = os.getenv("LLM_MODEL", "llama3.1:8b")
OLLAMA_URL = os.getenv("OLLAMA_URL", "http://localhost:11434")

ROOT = pathlib.Path(__file__).resolve().parents[1]
DISPLAY_MAP_PATH = ROOT / "data" / "display_names.json"
DATA_RAW = os.getenv("DATA_RAW", str(ROOT / "data" / "raw"))
DATA_CLEAN = os.getenv("DATA_CLEAN", str(ROOT / "data" / "clean"))


# ---------- session memory (optional, gated by ENABLE_DIALOG_MEMORY) ----------
ENABLE_DIALOG_MEMORY = os.getenv("ENABLE_DIALOG_MEMORY", "false").lower() in ("1", "true", "yes")
_session_memory = {}  # session_id -> deque(maxlen=6)
_session_order = []   # LRU order
_SESSION_MAX = 100

def get_session_id(request: Request) -> str | None:
    return request.headers.get("X-Session-ID")

def get_dialog(request: Request):
    if not ENABLE_DIALOG_MEMORY:
        return None
    session_id = get_session_id(request)
    if not session_id:
        return None
    # LRU cache logic
    mem = _session_memory.get(session_id)
    if mem is None:
        mem = deque(maxlen=6)
        _session_memory[session_id] = mem
        _session_order.append(session_id)
        if len(_session_order) > _SESSION_MAX:
            evict_id = _session_order.pop(0)
            _session_memory.pop(evict_id, None)
    else:
        # Move to end (most recently used)
        if session_id in _session_order:
            _session_order.remove(session_id)
        _session_order.append(session_id)
    return mem

# ---------- helpers for citations ----------
def display_name_for(source_path: str) -> str | None:
    try:
        mp = json.loads(DISPLAY_MAP_PATH.read_text(encoding="utf-8"))
        return mp.get(source_path)
    except Exception:
        return None

def build_urls(src: str):
    q = quote(src, safe="")
    return {
        "open_url": f"/v1/file?source_path={q}",
        "pdf_url": f"/v1/export/pdf?source_path={q}",
    }

# ---------- endpoints ----------
@app.get("/health")
def health():
    return {"ok": True}

@app.post("/v1/search", response_model=SearchResponse)
async def search(req: SearchRequest, request: Request):
    req_id = getattr(request.state, "request_id", None)
    try:
        raw_hits = search_chunks(req.query, req.k)
        hits = [
            SearchHit(
                text=h.get("text", ""),
                score=float(h.get("score", 0.0)),
                meta=h.get("meta", {}),
            )
            for h in raw_hits
        ]
        logger.info("search success", extra={"request_id": req_id, "module": __name__})
        resp = SearchResponse(results=hits)
        resp_dict = resp.dict()
        resp_dict["request_id"] = req_id
        return JSONResponse(resp_dict)
    except Exception as e:
        tb = traceback.format_exc()
        logger.error(f"search error: {e}", extra={"request_id": req_id, "module": __name__, "msg": tb})
        return JSONResponse({"error": str(e), "request_id": req_id}, status_code=500)

@app.get("/v1/ask")
def ask_get_hint():
    return {
        "hint": "Use POST /v1/ask with JSON body: {query, k, grounded_only, system?, model?}"
    }

@app.post("/v1/ask", response_model=AskResponse)
async def ask(payload: AskRequest, request: Request):

    req_id = getattr(request.state, "request_id", None)
    try:
        # Gather last Q/A from session memory if enabled
        dialog = get_dialog(request)
        last_user = dialog[-2] if dialog and len(dialog) >= 2 else None
        last_assistant = dialog[-1] if dialog and len(dialog) >= 1 else None

        # Define a minimal LLM call wrapper for rewriting
        async def rewriter_llm(messages):
            data = {"model": (payload.model or LLM_MODEL), "messages": messages, "stream": False}
            timeout_s = int(os.getenv("OLLAMA_TIMEOUT_SECONDS", "30"))
            async with httpx.AsyncClient(timeout=timeout_s) as client:
                resp = await client.post(f"{OLLAMA_URL}/api/chat", json=data)
                resp.raise_for_status()
                chunk = resp.json()
                return chunk.get("message", {}).get("content", "")

        import asyncio
        final_query = maybe_rewrite_query(
            last_user=last_user,
            last_assistant=last_assistant,
            new_user=payload.query,
            llm_call_fn=lambda messages: asyncio.run(rewriter_llm(messages)),
        )

        was_rewritten = (final_query.strip() != (payload.query or "").strip())
        logger.info(f"rewrite: {was_rewritten}", extra={"request_id": req_id, "module": __name__, "msg": f"raw={payload.query} final={final_query}"})

        # Determine k: request, env, or default
        k = payload.k if payload.k else int(os.getenv("ASK_TOP_K", "8"))
        try:
            hits = search_chunks(final_query, k)
        except Exception as e:
            tb = traceback.format_exc()
            logger.error(f"retriever error: {e}", extra={"request_id": req_id, "module": __name__, "msg": tb})
            return JSONResponse({"error": str(e), "request_id": req_id}, status_code=500)

        # Prepare top_chunks for prompt and citations
        top_chunks = []
        for h in hits:
            meta = h.get("meta", {})
            top_chunks.append({
                "chunk_id": meta.get("chunk_id"),
                "source_path": meta.get("source_path"),
                "title": meta.get("title", "Untitled"),
                "pages": meta.get("pages", ""),
                "content": h.get("text", "")
            })

        system_prompt = payload.system or build_system_prompt()
        answer = []

        # Grounded only logic
        if payload.grounded_only:
            if not hits:
                logger.info("ask grounded_only: no hits", extra={"request_id": req_id, "module": __name__})
                resp = AskResponse(answer="No relevant sources found for grounded-only mode.", citations=[])
                resp_dict = resp.dict()
                resp_dict["request_id"] = req_id
                return JSONResponse(resp_dict)
            messages = build_grounded_prompt(final_query, top_chunks, system_prompt)
            data = {"model": (payload.model or LLM_MODEL), "messages": messages, "stream": True}
        else:
            if not hits:
                final_answer = "⚠️ No sources found — answer not grounded.\n"
                try:
                    timeout_s = int(os.getenv("OLLAMA_TIMEOUT_SECONDS", "30"))
                    async with httpx.AsyncClient(timeout=timeout_s) as client:
                        resp = await client.post(f"{OLLAMA_URL}/api/chat", json={"model": (payload.model or LLM_MODEL), "messages": [
                            {"role": "system", "content": system_prompt},
                            {"role": "user", "content": f"Question: {final_query}"}
                        ], "stream": False})
                        resp.raise_for_status()
                        chunk = resp.json()
                        final_answer += chunk.get("message", {}).get("content", "")
                except Exception as e:
                    tb = traceback.format_exc()
                    logger.error(f"ollama error: {e}", extra={"request_id": req_id, "module": __name__, "msg": tb})
                    final_answer += "(LLM backend unavailable)"
                    resp = AskResponse(answer=final_answer, citations=[])
                    resp_dict = resp.dict()
                    resp_dict["request_id"] = req_id
                    return JSONResponse(resp_dict, status_code=500)
                resp = AskResponse(answer=final_answer, citations=[])
                resp_dict = resp.dict()
                resp_dict["request_id"] = req_id
                return JSONResponse(resp_dict)
            messages = build_grounded_prompt(final_query, top_chunks, system_prompt)
            data = {"model": (payload.model or LLM_MODEL), "messages": messages, "stream": True}

        try:
            timeout_s = int(os.getenv("OLLAMA_TIMEOUT_SECONDS", "30"))
            async with httpx.AsyncClient(timeout=timeout_s) as client:
                async with client.stream(
                    "POST", f"{OLLAMA_URL}/api/chat", json=data
                ) as resp:
                    resp.raise_for_status()
                    async for line in resp.aiter_lines():
                        if not line:
                            continue
                        try:
                            chunk = json.loads(line)
                            token = chunk.get("message", {}).get("content", "")
                            if token:
                                answer.append(token)
                        except json.JSONDecodeError:
                            continue
        except Exception as e:
            tb = traceback.format_exc()
            logger.error(f"ollama error: {e}", extra={"request_id": req_id, "module": __name__, "msg": tb})
            resp = AskResponse(answer=f"ERROR: {e}", citations=[])
            resp_dict = resp.dict()
            resp_dict["request_id"] = req_id
            return JSONResponse(resp_dict, status_code=500)

        # build enriched citations (include chunk_id/source_path)
        citations = []
        for i, chunk in enumerate(top_chunks):
            src = chunk.get("source_path", "")
            item = build_urls(src)
            item["display_name"] = display_name_for(src) or src
            item["chunk_id"] = chunk.get("chunk_id")
            item["source_path"] = src
            citations.append(item)

        final_answer = "".join(answer)
        if ENABLE_DIALOG_MEMORY and dialog is not None:
            try:
                dialog.append(payload.query)
                dialog.append(final_answer)
            except Exception:
                pass
        logger.info("ask success", extra={"request_id": req_id, "module": __name__})
        resp = AskResponse(answer=final_answer, citations=citations)
        resp_dict = resp.dict()
        resp_dict["request_id"] = req_id
        return JSONResponse(resp_dict)
    except Exception as e:
        tb = traceback.format_exc()
        logger.error(f"ask error: {e}", extra={"request_id": req_id, "module": __name__, "msg": tb})
        resp = AskResponse(answer=f"ERROR: {e}", citations=[])
        resp_dict = resp.dict()
        resp_dict["request_id"] = req_id
        return JSONResponse(resp_dict, status_code=500)

    # build enriched citations (include chunk_id/source_path)
    citations = []
    for i, chunk in enumerate(top_chunks):
        src = chunk.get("source_path", "")
        item = build_urls(src)
        item["display_name"] = display_name_for(src) or src
        item["chunk_id"] = chunk.get("chunk_id")
        item["source_path"] = src
        citations.append(item)

    final_answer = "".join(answer)
    try:
        _dialog.append(payload.query)
        _dialog.append(final_answer)
    except Exception:
        pass
    return AskResponse(answer=final_answer, citations=citations)


# --- Normalized file serving endpoint ---
@app.get("/v1/file", response_class=PlainTextResponse)
def get_file(path: str = Query(..., description="Source-relative path (raw or clean). Anchor (#...) is allowed and ignored by the server).")):
    if not path:
        raise HTTPException(status_code=400, detail="Missing 'path' query param")
    try:
        resolved, anchor = normalize_source_path(path)
    except PathResolutionError as e:
        raise HTTPException(status_code=404, detail=str(e))
    try:
        text = resolved.read_text(encoding="utf-8", errors="ignore")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to read file: {e}")
    return text

def _markdown_body_for_source(source_path: str) -> str:
    texts = []
    for p in pathlib.Path(DATA_CLEAN).rglob("*.md"):
        raw = p.read_text(encoding="utf-8")
        if raw.startswith("---") and f"source_path: {source_path}" in raw:
            body = raw.split("---", 2)[2]
            texts.append(body.strip())
    return "\n\n".join(texts) if texts else ""

@app.get("/v1/export/pdf")
def export_pdf(source_path: str = Query(...)):
    if not _HAS_REPORTLAB:
        return JSONResponse(
            {"error": "PDF export requires reportlab. Please install it: pip install reportlab"},
            status_code=406,
        )
    body = _markdown_body_for_source(source_path)
    if not body:
        return JSONResponse(
            {"error": "No cleaned content found for source"}, status_code=404
        )
    # PDF generation only if reportlab is available
    from reportlab.lib.pagesizes import LETTER
    from reportlab.pdfgen import canvas
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
        headers={"Content-Disposition": f'attachment; filename=\"{filename}\"'},
    )