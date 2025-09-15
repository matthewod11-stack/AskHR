# app/store.py
import os
import chromadb
from dotenv import load_dotenv

load_dotenv()

CHROMA_PATH = os.getenv("CHROMA_PATH", "./index")
COLLECTION_NAME = os.getenv("COLLECTION_NAME", "hr_corpus")

_client = None
_collection = None

def get_client():
    global _client
    if _client is None:
        _client = chromadb.PersistentClient(path=CHROMA_PATH)
    return _client

def get_collection():
    global _collection
    if _collection is not None:
        return _collection
    client = get_client()
    # get or create
    try:
        _collection = client.get_collection(COLLECTION_NAME)
    except Exception:
        _collection = client.create_collection(COLLECTION_NAME)
    return _collection

def reset_collection():
    """Danger: deletes and recreates the collection."""
    client = get_client()
    try:
        client.delete_collection(COLLECTION_NAME)
    except Exception:
        pass
    return client.create_collection(COLLECTION_NAME)

