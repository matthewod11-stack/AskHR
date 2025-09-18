from __future__ import annotations
import os, requests
from typing import List, Dict, Any

OLLAMA_URL = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")
EMBED_MODEL = os.getenv("OLLAMA_EMBED_MODEL", "nomic-embed-text")
CHAT_MODEL = os.getenv("OLLAMA_CHAT_MODEL", "llama3.1:8b")
TIMEOUT = int(os.getenv("OLLAMA_TIMEOUT_SECONDS", "60"))

def embed_text(text: str) -> List[float]:
    try:
        r = requests.post(
            f"{OLLAMA_URL}/api/embeddings",
            json={"model": EMBED_MODEL, "prompt": text},
            timeout=TIMEOUT,
        )
        r.raise_for_status()
        data = r.json()
        embedding = data.get("embedding") or (data.get("data") or [{}])[0].get("embedding")
        if isinstance(embedding, list):
            return embedding
        else:
            return []
    except Exception:
        return []

    def embed_texts(texts: List[str]) -> List[List[float]]:
        return [embed_text(t) for t in texts]

    def _messages_to_prompt(messages: List[Dict[str, str]]) -> str:
        # Convert chat messages into a single plain prompt for /api/generate fallback
        parts = []
        for m in messages:
            role = m.get("role","user")
            content = m.get("content","")
            if role == "system":
                parts.append(f"[SYSTEM]\n{content}\n")
            elif role == "assistant":
                parts.append(f"[ASSISTANT]\n{content}\n")
            else:
                parts.append(f"[USER]\n{content}\n")
        parts.append("\n[ASSISTANT]\n")
        return "\n".join(parts).strip()

    def chat_with_model(messages: List[Dict[str, str]]) -> str:
        """
        Try /api/chat first. If no content returned, fall back to /api/generate with a flattened prompt.
        """
        # --- attempt 1: /api/chat ---
        try:
            r = requests.post(
                f"{OLLAMA_URL}/api/chat",
                json={"model": CHAT_MODEL, "messages": messages, "stream": False},
                timeout=TIMEOUT,
            )
            r.raise_for_status()
            data = r.json()
            msg = data.get("message") or {}
            if isinstance(msg, dict):
                content = msg.get("content")
                if isinstance(content, str) and content.strip():
                    return content.strip()
            # sometimes content is under 'response'
            resp = data.get("response") or data.get("text")
            if isinstance(resp, str) and resp.strip():
                return resp.strip()
        except Exception:
            # fall through to generate
            pass

        # --- attempt 2: /api/generate ---
        prompt = _messages_to_prompt(messages)
        try:
            r2 = requests.post(
                f"{OLLAMA_URL}/api/generate",
                json={"model": CHAT_MODEL, "prompt": prompt, "stream": False},
                timeout=TIMEOUT,
            )
            r2.raise_for_status()
            d2 = r2.json()
            out = d2.get("response") or d2.get("text") or ""
            return (out or "").strip()
        except Exception:
            return ""

