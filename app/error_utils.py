from __future__ import annotations
import uuid
import logging
from typing import Tuple, Dict, Any

log = logging.getLogger("askhr")

def get_request_id(headers: Dict[str, Any]) -> str:
    # Reuse incoming header if present; otherwise generate.
    rid = headers.get("x-request-id") or headers.get("X-Request-ID")
    return rid if isinstance(rid, str) and rid.strip() else str(uuid.uuid4())

def safe_response(payload: Dict[str, Any], request_id: str) -> Dict[str, Any]:
    # Ensure stable /v1/ask contract
    base = {
        "answer": payload.get("answer", "") or "",
        "citations": payload.get("citations", []) or [],
        "ungrounded": bool(payload.get("ungrounded", False)),
        "request_id": request_id,
    }
    # optional error for UI
    if payload.get("error"):
        base["error"] = str(payload["error"])
    return base