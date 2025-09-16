import os, json, httpx, pathlib
from urllib.parse import quote
from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse, StreamingResponse, JSONResponse
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
from app.prompting import build_system_prompt, maybe_rewrite_query, build_user_prompt

load_dotenv()
app = FastAPI(title="Ask HR (Local)")
app.add_middleware(
    CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"]
)

LLM_MODEL = os.getenv("LLM_MODEL", "llama3.1:8b")
OLLAMA_URL = os.getenv("OLLAMA_URL", "http://localhost:11434")

ROOT = pathlib.Path(__file__).resolve().parents[1]
DISPLAY_MAP_PATH = ROOT / "data" / "display_names.json"
DATA_RAW = os.getenv("DATA_RAW", str(ROOT / "data" / "raw"))
DATA_CLEAN = os.getenv("DATA_CLEAN", str(ROOT / "data" / "clean"))

# ---------- conversation memory (minimal) ----------
_dialog = deque(maxlen=6)  # last 3 Q/A pairs (Q,A,Q,A,...)
def rewrite(question: str) -> str:
    """
    Minimal query rewrite: include the last QA context as a hint so the retriever
    and the model have continuity. This is deliberately light-weight and local.
    """
    if len(_dialog) < 2:
        return question
    last_a = _dialog[-1]
    last_q = _dialog[-2] if len(_dialog) >= 2 else None
    if last_q and last_a:
        return (f"{question}\n\n(Previous Q: {last_q[:300]})\n(Previous A summary: {last_a[:500]})")
    return question


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
def search(req: SearchRequest):
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
        return SearchResponse(results=hits)
    except Exception:
        return SearchResponse(results=[])


@app.get("/v1/ask")
def ask_get_hint():
    return {
        "hint": "Use POST /v1/ask with JSON body: {query, k, grounded_only, system?, model?}"
    }


@app.post("/v1/ask", response_model=AskResponse)
async def ask(payload: AskRequest) -> AskResponse:
    # Gather last Q/A from dialog memory
    last_user = _dialog[-2] if len(_dialog) >= 2 else None
    last_assistant = _dialog[-1] if len(_dialog) >= 1 else None

    # Define a minimal LLM call wrapper for rewriting
    async def rewriter_llm(messages):
        # Use Ollama chat API, return only the text output
        data = {"model": (payload.model or LLM_MODEL), "messages": messages, "stream": False}
        async with httpx.AsyncClient(timeout=None) as client:
            resp = await client.post(f"{OLLAMA_URL}/api/chat", json=data)
            resp.raise_for_status()
            chunk = resp.json()
            return chunk.get("message", {}).get("content", "")

    # Rewrite query if needed
    import logging
    logger = logging.getLogger("askhr")
    import asyncio
    final_query = maybe_rewrite_query(
        last_user=last_user,
        last_assistant=last_assistant,
        new_user=payload.query,
        llm_call_fn=lambda messages: asyncio.run(rewriter_llm(messages)),
    )
    user_prompt = build_user_prompt(final_query)

    was_rewritten = (final_query.strip() != (payload.query or "").strip())
    logger.info("rewrite=%s raw=%r final=%r", was_rewritten, payload.query, final_query)

    hits = search_chunks(final_query, payload.k)
    if not hits:
        return AskResponse(answer="I didn’t find relevant context.", citations=[])

    system_prompt = payload.system or build_system_prompt()
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt},
    ]
    data = {"model": (payload.model or LLM_MODEL), "messages": messages, "stream": True}
    answer = []

    try:
        async with httpx.AsyncClient(timeout=None) as client:
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
    except Exception:
        raise HTTPException(status_code=502, detail="LLM backend unavailable")

    # build enriched citations
    citations = []
    for h in hits:
        src = h["meta"].get("source_path", "")
        item = build_urls(src)
        item["display_name"] = display_name_for(src) or src
        citations.append(item)

    final_answer = "".join(answer)
    # update simple dialog memory (store the raw user Q and the final answer)
    try:
        _dialog.append(payload.query)
        _dialog.append(final_answer)
    except Exception:
        pass
    return AskResponse(answer=final_answer, citations=citations)


# ---------- file serving endpoints ----------
@app.get("/v1/file")
def serve_file(source_path: str = Query(..., description="Path relative to data/raw")):
    full = pathlib.Path(DATA_RAW) / source_path
    full = full.resolve()
    if not str(full).startswith(str(pathlib.Path(DATA_RAW).resolve())) or not full.exists():
        return JSONResponse({"error": "Not found"}, status_code=404)
    return FileResponse(str(full), filename=full.name, media_type="application/octet-stream")


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
        headers={"Content-Disposition": f'attachment; filename="{filename}"'},
    )
