# app/llm.py
from __future__ import annotations
from typing import List, Dict
import os, requests

OLLAMA_URL = os.getenv("OLLAMA_URL", "http://localhost:11434")
ASK_MODEL  = os.getenv("ASK_MODEL",  "llama3.1:8b")

def chat_with_model(messages: List[Dict[str, str]]) -> str:
    """
    Call Ollama's /api/chat with a standard messages list:
    [{"role":"system","content":"..."}, {"role":"user","content":"..."}]
    """
    r = requests.post(
        f"{OLLAMA_URL}/api/chat",
        json={"model": ASK_MODEL, "messages": messages, "stream": False},
        timeout=120,
    )
    r.raise_for_status()
    data = r.json()
    return (data.get("message") or {}).get("content", "") or ""
