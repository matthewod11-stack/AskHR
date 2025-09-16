from pydantic import BaseModel, Field
from typing import List

class CaseRow(BaseModel):
    id: str
    question: str
    must_have: List[str]
    min_citations: int = Field(default=2)
    k: int = Field(default=8)

class CaseResult(BaseModel):
    id: str
    coverage_pct: float
    citations_count: int
    latency_ms: float
    pass_case: bool
    answer_len: int

class Summary(BaseModel):
    total_cases: int
    avg_coverage_pct: float
    pct_cases_ge80_coverage: float
    pct_answers_ge2_citations: float
    avg_latency_ms: float
    pct_passed: float
    acceptance: bool

def compute_acceptance(summary: Summary) -> bool:
    return summary.pct_passed >= 80 and summary.pct_answers_ge2_citations >= 90
