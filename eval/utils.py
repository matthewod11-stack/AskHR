# eval/utils.py

import csv
import json
import os
import re
import time
from typing import Any, Dict, List, Optional, Sequence, Tuple

import requests

from .schema import CaseRow, coerce_bool

_REQUIRED_HEADERS: Tuple[str, ...] = ("id", "query", "expect_grounded", "notes")


def _validate_headers(fieldnames: Optional[Sequence[str]]) -> None:
    """
    DictReader.fieldnames is Optional[Sequence[str]] until the reader is consumed.
    Accept Optional, guard None, and raise a friendly error if headers are missing.
    """
    if not fieldnames:
        raise ValueError(
            "Eval CSV has no header row. Expected headers: " + ", ".join(_REQUIRED_HEADERS)
        )
    fn = [f.strip() for f in fieldnames]
    missing = [h for h in _REQUIRED_HEADERS if h not in fn]
    if missing:
        raise ValueError(
            f"Eval CSV is missing required header(s): {', '.join(missing)}. "
            f"Expected headers: {', '.join(_REQUIRED_HEADERS)}"
        )


def load_cases(path: str) -> List[CaseRow]:
    rows: List[CaseRow] = []
    with open(path, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        _validate_headers(reader.fieldnames)
        for raw in reader:
            rid = (raw.get("id") or "").strip()
            q = (raw.get("query") or "").strip()
            eg = coerce_bool(raw.get("expect_grounded"))
            notes = (raw.get("notes") or "").strip()
            # Parse keywords column (semicolon or comma separated)
            kw_raw = (raw.get("keywords") or "").strip()
            keywords = None
            if kw_raw:
                keywords = [k.strip() for k in re.split(r"[;,]", kw_raw) if k.strip()]
            rows.append(
                CaseRow(id=rid, query=q, expect_grounded=eg, notes=notes, keywords=keywords)
            )
    return rows


def normalize(text: str) -> str:
    return re.sub(r"\s+", " ", text.strip().lower())


def score_keywords(answer: str, keywords: List[str]) -> float:
    answer_norm = normalize(answer)
    found = sum(1 for kw in keywords if kw.lower() in answer_norm)
    return 100.0 * found / max(1, len(keywords))


def post_ask(api_url: str, query: str, k: int, timeout: int) -> Dict[str, Any]:
    payload = {"query": query, "k": k}
    resp = requests.post(api_url, json=payload, timeout=timeout)
    resp.raise_for_status()
    return resp.json()


def timestamp_dir(base: str = "eval/results") -> str:
    ts = time.strftime("%Y%m%d-%H%M")
    path = os.path.join(base, ts)
    os.makedirs(path, exist_ok=True)
    return path


def write_csv(path: str, rows: Sequence[Dict[str, Any]]) -> None:
    if not rows:
        return
    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        for row in rows:
            writer.writerow(row)


def write_json(path: str, data: Dict[str, Any]) -> None:
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)


def exponential_backoff(attempt: int, base: float = 0.5) -> float:
    return base * (2**attempt)
