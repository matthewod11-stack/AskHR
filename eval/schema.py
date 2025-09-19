from dataclasses import dataclass
from typing import Optional, List


def coerce_bool(v) -> bool:
    s = str(v).strip().lower()
    if s in {"1", "true", "t", "yes", "y"}:
        return True
    if s in {"0", "false", "f", "no", "n", ""}:
        return False
    return False


@dataclass
class CaseRow:
    id: str
    query: str
    expect_grounded: bool
    notes: Optional[str] = ""
    keywords: Optional[List[str]] = None


## Removed unused EvalCase, EvalResult, EvalSummary for harness CSV loading
