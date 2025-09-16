# app/schemas.py
from __future__ import annotations
from typing import Optional, Dict, List
from pydantic import BaseModel


class SearchRequest(BaseModel):
    query: str
    k: int = 8


class SearchHit(BaseModel):
    text: str
    score: float
    meta: Dict


class SearchResponse(BaseModel):
    results: List[SearchHit]


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
    citations: List[Citation] = []
