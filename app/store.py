import os
import chromadb
from dotenv import load_dotenv

load_dotenv()

CHROMA_DIR = os.getenv("CHROMA_DIR", "./index")
_CLIENT = chromadb.PersistentClient(path=CHROMA_DIR)
_COLLECTION = "hr_corpus"


def get_collection():
    return _CLIENT.get_or_create_collection(_COLLECTION)


def reset_collection():
    try:
        _CLIENT.delete_collection(_COLLECTION)
    except Exception:
        pass
    return get_collection()
