
from __future__ import annotations
import os
from functools import lru_cache
from typing import Optional

import chromadb
from chromadb.config import Settings

# Environment
PERSIST_DIR = os.getenv("CHROMA_PERSIST_DIR", os.getenv("CHROMA_DIR", "index"))
COLLECTION_NAME = os.getenv("CHROMA_COLLECTION", "askhr")

# We DO NOT set an embedding_function here on purpose.
# All embeddings must be provided explicitly to avoid dimension mismatch.
@lru_cache(maxsize=1)
def get_client() -> chromadb.Client: # type: ignore
    return chromadb.Client(
        Settings(
            persist_directory=PERSIST_DIR,
            anonymized_telemetry=False,
        )
    )

def get_persist_dir() -> str:
    return PERSIST_DIR

def get_collection_name() -> str:
    return COLLECTION_NAME

@lru_cache(maxsize=1)
def get_collection():
    client = get_client()
    # No embedding_function; ensure distance metric is consistent (cosine)
    return client.get_or_create_collection(
        name=COLLECTION_NAME,
        metadata={"hnsw:space": "cosine"},
        embedding_function=None,
    )

def persist() -> None:
    try:
        get_client().persist()
    except Exception:
        # Older clients may not require/implement persist(); ignore.
        pass
