from pydantic import BaseModel, Field
from typing import Optional, Dict, List

class SearchRequest(BaseModel):
    query: str
    k: int = 8

class SearchHit(BaseModel):
    text: str
    score: float
    meta: Dict

class SearchResponse(BaseModel):
    results: List[SearchHit] = Field(default_factory=list)

class AskRequest(BaseModel):
    query: str
    k: int = 8
    system: Optional[str] = None
    grounded_only: bool = False
    model: Optional[str] = None

class Citation(BaseModel):
    display_name: Optional[str] = None
    open_url: Optional[str] = None
    pdf_url: Optional[str] = None

class AskResponse(BaseModel):
    answer: str
    citations: List[Citation] = Field(default_factory=list)