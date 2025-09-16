# app/embeddings.py
import os
import httpx
from dotenv import load_dotenv

# Load .env (safe to call multiple times)
load_dotenv()

EMBED_MODEL = os.getenv("EMBED_MODEL", "nomic-embed-text")
OLLAMA_URL = os.getenv("OLLAMA_URL", "http://localhost:11434")

def get_embedding(text: str) -> list[float]:
    with httpx.Client(timeout=60) as c:
        r = c.post(f"{OLLAMA_URL}/api/embeddings",
                   json={"model": EMBED_MODEL, "prompt": text})
        r.raise_for_status()
        return r.json()["embedding"]

# Optional helper if you want to know the vector size
_emb_dim = None
def embedding_dim() -> int:
    global _emb_dim
    if _emb_dim is None:
        _emb_dim = len(get_embedding("dimension probe"))
    return _emb_dim

