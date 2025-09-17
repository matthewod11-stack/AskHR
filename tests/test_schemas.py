import pytest
from app.schemas import AskResponse

def test_askresponse_citations_independent():
    r1 = AskResponse(answer="a")
    r1.citations.append("c1") # type: ignore
    r2 = AskResponse(answer="b")
    assert r2.citations == []
