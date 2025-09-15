# app/retriever.py
from typing import List, Dict, Any
from app.store import get_collection
from app.embeddings import get_embedding

def search_chunks(query: str, k: int = 8) -> List[Dict[str, Any]]:
    """
    Returns a list of dicts: {text, distance, meta}
    Note: In Chroma, lower distance means closer match.
    """
    col = get_collection()
    qvec = get_embedding(query)
    res = col.query(
        query_embeddings=[qvec],
        n_results=k,
        include=["documents", "metadatas", "distances"],
    )
    out = []
    if not res["ids"]:
        return out
    for i in range(len(res["ids"][0])):
        out.append({
            "text": res["documents"][0][i],
            "distance": float(res["distances"][0][i]),
            "meta": res["metadatas"][0][i],
        })
    # sort ascending by distance (best first)
    out.sort(key=lambda x: x["distance"])
    return out
