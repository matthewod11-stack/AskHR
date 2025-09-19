from __future__ import annotations
from typing import Dict, Any

# Reserved attributes on LogRecord that cannot appear in `extra`
# (subset; we only need to avoid known collisions)
_RESERVED = {
    "name",
    "msg",
    "args",
    "levelname",
    "levelno",
    "pathname",
    "filename",
    "module",
    "exc_info",
    "exc_text",
    "stack_info",
    "lineno",
    "funcName",
    "created",
    "msecs",
    "relativeCreated",
    "thread",
    "threadName",
    "processName",
    "process",
    "message",
    "asctime",
}


def safe_extra(extra: Dict[str, Any] | None) -> Dict[str, Any]:
    if not extra:
        return {}
    out: Dict[str, Any] = {}
    for k, v in extra.items():
        if k in _RESERVED:
            if k == "module":
                out["modulename"] = v  # common case
            else:
                out[f"x_{k}"] = v
        else:
            out[k] = v
    return out
