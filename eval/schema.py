from dataclasses import dataclass
from typing import List

@dataclass
class CaseRow:
    id: str
    question: str
    must_have: List[str]
    min_citations: int
    k: int

from typing import Optional, List, Dict, Any
from pydantic import BaseModel, Field

class EvalCase(BaseModel):
    id: str
    query: str
    expect_grounded: bool = False
    notes: Optional[str] = None

class EvalResult(BaseModel):
    id: str
    query: str
    answer: str
    citations: List[str] = Field(default_factory=list)
    grounded: bool
    passed: bool
    meta: Dict[str, Any] = Field(default_factory=dict)

class EvalSummary(BaseModel):
    total: int
    passed: int
    failed: int
    grounded_rate: float
