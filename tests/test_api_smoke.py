from fastapi.testclient import TestClient
import importlib

# Import app and patch deps on the module where they're used
m = importlib.import_module("app.main")  # m.app is FastAPI()

client = TestClient(m.app)


def test_health_ok():
    res = client.get("/health")
    assert res.status_code == 200


def test_ask_smoke_with_mocks(monkeypatch):
    # Patch the chat call so we don't hit Ollama
    if hasattr(m, "embeddings") and hasattr(m.embeddings, "chat_with_model"):
        monkeypatch.setattr(
            m.embeddings, "chat_with_model", lambda messages: "stub-answer", raising=True
        )

    # Best-effort: if a retriever module is imported in app.main, return no chunks
    if hasattr(m, "retriever"):
        # support various function names; patch whichever exists
        for fn in ("retrieve", "retrieve_top_k", "get_top_k", "query"):
            if hasattr(m.retriever, fn):
                monkeypatch.setattr(m.retriever, fn, lambda *a, **kw: [], raising=False)

    res = client.post("/v1/ask", json={"query": "ping", "k": 1})
    assert res.status_code == 200
    data = res.json()
    assert isinstance(data, dict)
    assert "answer" in data and "citations" in data
