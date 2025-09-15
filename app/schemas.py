# app/schemas.py
from pydantic import BaseModel
from typing import List, Dict, Any

class SearchRequest(BaseModel):
    query: str
    k: int = 8

class SearchHit(BaseModel):
    text: str
    distance: float
    meta: Dict[str, Any]


class SearchResponse(BaseModel):
    results: List[SearchHit]

class AskRequest(BaseModel):
    """
    Request model for /v1/ask endpoint.
    """
    query: str
    k: int = 8

class AskResponse(BaseModel):
    """
    Response model for /v1/ask endpoint.
    """
    answer: str
    citations: List[str] = []
