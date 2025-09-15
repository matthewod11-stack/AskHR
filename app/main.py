# app/main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
import os

from app.schemas import SearchRequest, SearchResponse, SearchHit, AskRequest, AskResponse
from app.retriever import search_chunks
from app.prompting import build_system_prompt, build_user_prompt
import httpx
from fastapi import HTTPException


load_dotenv()


app = FastAPI(title="HR Ask Local")

# (Optional) allow Streamlit to call this API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8501", "http://127.0.0.1:8501"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/health")
def health():
    """Health check endpoint."""
    return {"ok": True}


@app.post("/v1/search", response_model=SearchResponse)
def search(payload: SearchRequest):
    """Search endpoint for chunk retrieval."""
    hits = search_chunks(payload.query, payload.k)
    return SearchResponse(results=[
        SearchHit(text=h["text"], distance=h["distance"], meta=h["meta"])
        for h in hits
    ])


# --- Answering Endpoint ---
LLM_MODEL = os.getenv("LLM_MODEL", "llama3.1:8b")
OLLAMA_URL = os.getenv("OLLAMA_URL", "http://localhost:11434")

@app.post("/v1/ask", response_model=AskResponse)
async def ask(payload: AskRequest) -> AskResponse:
    """
    Answering endpoint using local RAG and Ollama LLM.
    Retrieves context, builds prompts, and returns answer with citations.
    """
    hits = search_chunks(payload.query, payload.k)
    if not hits:
        return AskResponse(answer="I didn’t find relevant context.", citations=[])

    system_prompt = build_system_prompt()
    user_prompt = build_user_prompt(payload.query, hits)

    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt}
    ]
    data = {
        "model": LLM_MODEL,
        "messages": messages
    }
    try:
        async with httpx.AsyncClient(timeout=120) as client:
            resp = await client.post(f"{OLLAMA_URL}/api/chat", json=data)
            resp.raise_for_status()
            result = resp.json()
            answer = result.get("message", {}).get("content", "")
    except Exception:
        raise HTTPException(status_code=502, detail="LLM backend unavailable")

    citations = [h["meta"].get("source", "") for h in hits]
    return AskResponse(answer=answer, citations=citations)

# --- Quick Test Examples ---
# Health
# curl -s http://localhost:8000/health | jq
#
# Search sanity
# curl -s -X POST http://localhost:8000/v1/search \
#   -H "content-type: application/json" \
#   -d '{"query":"PIP outline for low-pipeline AE","k":5}' | jq '.results[0]'
#
# Ask end-to-end
# curl -s -X POST http://localhost:8000/v1/ask \
#   -H "content-type: application/json" \
#   -d '{"query":"Draft a PIP outline for a low-pipeline AE and cite sources.","k":8}' | jq
