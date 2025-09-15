# app/embeddings.py
import os
import httpx
from dotenv import load_dotenv

# Load .env (safe to call multiple times)
load_dotenv()

EMBED_MODEL = os.getenv("EMBED_MODEL", "nomic-embed-text")
OLLAMA_URL = os.getenv("OLLAMA_URL", "http://localhost:11434")

def get_embedding(text: str) -> list[float]:
    """Return a single vector embedding from the local Ollama embedding model."""
    if not text or not text.strip():
        return []
    payload = {"model": EMBED_MODEL, "prompt": text}
    with httpx.Client(timeout=60) as client:
        r = client.post(f"{OLLAMA_URL}/api/embeddings", json=payload)
        r.raise_for_status()
        data = r.json()
    vec = data.get("embedding", [])
    return vec

# Optional helper if you want to know the vector size
_emb_dim = None
def embedding_dim() -> int:
    global _emb_dim
    if _emb_dim is None:
        _emb_dim = len(get_embedding("dimension probe"))
    return _emb_dim

