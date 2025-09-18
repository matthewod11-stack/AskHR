from __future__ import annotations
from dataclasses import dataclass, asdict
from typing import List, Optional, Dict, Any

@dataclass
class EvalCase:
    id: str
    query: str
    k: int = 8
    grounded_only: bool = False
    expect_any_of: Optional[List[str]] = None  # substrings expected in citations or answer
    min_citations: int = 0
    notes: str = ""

    @staticmethod
    def from_row(row: Dict[str, str]) -> "EvalCase":
        def as_bool(s: str) -> bool:
            return str(s).strip().lower() in ("true","1","yes","y")
        expects = [s.strip() for s in str(row.get("expect_any_of","")) .split(";") if s.strip()]
        return EvalCase(
            id=str(row.get("id","")) .strip(),
            query=str(row.get("query","")) .strip(),
            k=int(row.get("k", 8) or 8),
            grounded_only=as_bool(row.get("grounded_only","false")),
            expect_any_of=expects or [],
            min_citations=int(row.get("min_citations", 0) or 0),
            notes=str(row.get("notes","")) .strip(),
        )

@dataclass
class EvalResult:
    id: str
    query: str
    answer_tokens: int
    citations: List[str]
    grounded: bool
    hit: bool               # any expected substring found (in citations or answer)
    precision_proxy: float  # matched_citations / max(1, len(citations))
    elapsed_ms: int
    status: str             # "ok" or "error"
    error: Optional[str] = None
    meta: Optional[Dict[str, Any]] = None

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)

@dataclass
class EvalSummary:
    total: int
    answered: int
    grounded_rate: float
    hit_rate: float
    avg_precision_proxy: float
    avg_answer_tokens: float

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)
