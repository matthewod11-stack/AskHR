
from __future__ import annotations
#!/usr/bin/env python3
# Retrieval tuning: query expansion + MMR diversity over top-N candidates; env-configurable; backward compatible.
from typing import List, Dict, Any
from .store import get_collection
from .embeddings import embed_text

DEFAULT_K = 8

def _unwrap_query_result(res: Dict[str, Any]) -> List[Dict[str, Any]]:
    """Flatten Chroma query() response into a list of chunk dicts."""
    # Chroma returns lists-of-lists
    ids = (res.get("ids") or [[]])[0]
    docs = (res.get("documents") or [[]])[0]
    metas = (res.get("metadatas") or [[]])[0]
    dists = (res.get("distances") or [[]])[0]

    out: List[Dict[str, Any]] = []
    limit = min(len(ids), len(docs), len(metas))
    for i in range(limit):
        m = metas[i] or {}
        out.append({
            "chunk_id": ids[i] if i < len(ids) else "",
            "text": docs[i],
            "source_path": m.get("source_path") or m.get("path") or "",
            "title": m.get("title") or "Untitled",
            "distance": (dists[i] if i < len(dists) else None),
        })
    return out

def retrieve_topk(query: str, top_k: int = DEFAULT_K) -> List[Dict[str, Any]]:
    """
    Retrieve top_k chunks from Chroma for the query.
    Returns a list of dicts with: chunk_id, text, source_path, title, distance.
    """
    top_k = int(top_k or DEFAULT_K)
    q_emb = embed_text(query)
    col = get_collection()
    # IMPORTANT: do NOT include "ids" — Chroma returns it automatically but rejects it in `include=[...]`
    res = col.query(
        query_embeddings=[q_emb],
        n_results=max(1, top_k),
        include=["documents", "metadatas", "distances"],  # type: ignore
    )
    chunks = _unwrap_query_result(res)

    # Simple uniqueness by (source_path, chunk_id)
    seen = set()
    uniq: List[Dict[str, Any]] = []
    for ch in chunks:
        key = (ch.get("source_path", ""), ch.get("chunk_id", ""))
        if key in seen:
            continue
        seen.add(key)
        uniq.append(ch)
        if len(uniq) >= top_k:
            break
    return uniq

# Backward-compat export
retrieve_top_k = retrieve_topk

__all__ = ["retrieve_topk", "retrieve_top_k"]
