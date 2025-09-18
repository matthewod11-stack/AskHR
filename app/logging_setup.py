from __future__ import annotations
import json
import logging
import os
import sys
from datetime import datetime

class _JsonFormatter(logging.Formatter):
    def format(self, record: logging.LogRecord) -> str:
        payload = {
            "ts": datetime.utcnow().isoformat(timespec="microseconds") + "Z",
            "level": record.levelname,
            "logger": record.name,
            "msg": record.getMessage(),
            "module": record.module,
        }
        # include request_id if middleware set it via `extra={"request_id": ...}`
        rid = getattr(record, "request_id", None) or getattr(record, "rid", None)
        if rid:
            payload["request_id"] = str(rid)
        return json.dumps(payload, ensure_ascii=False)

def configure_json_logging(level: str | int | None = None) -> None:
    """
    Configure root logging with a JSON formatter (stdout).
    Usage: from app.logging_setup import configure_json_logging; configure_json_logging()
    """
    lvl_name = (level or os.getenv("LOG_LEVEL", "INFO"))
    try:
        lvl = int(lvl_name)
    except Exception:
        lvl = getattr(logging, str(lvl_name).upper(), logging.INFO)

    root = logging.getLogger()
    root.setLevel(lvl)

    # prevent duplicate handlers on reloads
    for h in list(root.handlers):
        root.removeHandler(h)

    handler = logging.StreamHandler(stream=sys.stdout)
    handler.setFormatter(_JsonFormatter())
    root.addHandler(handler)

    # tame noisy libraries
    logging.getLogger("uvicorn.access").handlers = []   # drop default access logs
    logging.getLogger("uvicorn.error").setLevel(lvl)
    logging.getLogger("uvicorn").setLevel(lvl)

__all__ = ["configure_json_logging"]
