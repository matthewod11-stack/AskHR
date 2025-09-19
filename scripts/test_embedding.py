# scripts/test_embedding.py
from app.embeddings import get_embedding, embedding_dim

v = get_embedding("HR test: how to structure a PIP")
print("Embedding length:", embedding_dim())
print("First 8 numbers:", v[:8])
