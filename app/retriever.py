#!/usr/bin/env python3
# Retrieval tuning: query expansion + MMR diversity over top-N candidates; env-configurable; backward compatible.
from __future__ import annotations

import os
from typing import Any, Dict, List
import math

# HR synonym expansion
_HR_SYNONYMS = {
    "pip": ["performance improvement plan","coaching plan","corrective action"],
    "performance review": ["appraisal","evaluation","calibration","review cycle"],
    "progressive discipline": ["disciplinary action","written warning","final warning"],
    "leave": ["pto","time off","absence","fmla"],
    "termination": ["separation","dismissal","exit","involuntary"],
    "onboarding": ["new hire","orientation","ramp","30-60-90","306090"],
    "compensation": ["pay","salary","band","range","total rewards"],
    "job description": ["jd","role profile","position description"],
}

def expand_query(q: str, max_terms: int = 6) -> str:
    ql = q.lower()
    extras = []
    for k,syns in _HR_SYNONYMS.items():
        if k in ql or any(s in ql for s in syns):
            extras.extend(syns)
    extras = list(dict.fromkeys(extras))[:max_terms]
    return q if not extras else f"{q} :: {' | '.join(extras)}"

def cosine(a, b):
    # Pure python cosine similarity
    if not a or not b or len(a) != len(b): return 0.0
    dot = sum(x*y for x, y in zip(a, b))
    norm_a = math.sqrt(sum(x*x for x in a))
    norm_b = math.sqrt(sum(y*y for y in b))
    if norm_a == 0 or norm_b == 0: return 0.0
    return dot / (norm_a * norm_b)

def mmr_select(query_vec, cand_vecs, cand_payloads, k, lambda_diversity):
    # Maximal Marginal Relevance selection
    selected, selected_idx = [], set()
    if not cand_vecs: return []
    scores = [cosine(query_vec, v) for v in cand_vecs]
    # Start with highest score
    for _ in range(min(k, len(cand_vecs))):
        if not selected:
            idx = max(range(len(scores)), key=lambda i: scores[i])
            selected.append(idx)
            selected_idx.add(idx)
            continue
        # For each candidate, compute MMR score
        mmr_scores = []
        for i, v in enumerate(cand_vecs):
            if i in selected_idx: mmr_scores.append(float('-inf'))
            else:
                sim_to_query = cosine(query_vec, v)
                sim_to_selected = max([cosine(v, cand_vecs[j]) for j in selected_idx], default=0.0)
                mmr_score = lambda_diversity * sim_to_query - (1 - lambda_diversity) * sim_to_selected
                mmr_scores.append(mmr_score)
        idx = max(range(len(mmr_scores)), key=lambda i: mmr_scores[i])
        selected.append(idx)
        selected_idx.add(idx)
    return [cand_payloads[i] for i in selected]


from app.store import get_collection
from app.embeddings import get_embedding
try:
    from chromadb.api.types import IncludeEnum
except ImportError:
    IncludeEnum = None


def _include_arg():
    """
    Chroma's include can be either strings or IncludeEnum depending on version.
    This returns a compatible list without importing version-specific types.
    """
    # Return IncludeEnum values if available, else fallback to strings
    if IncludeEnum:
        return [IncludeEnum.documents, IncludeEnum.metadatas, IncludeEnum.distances]
    return ["documents", "metadatas", "distances"]



def search_chunks(query: str, k: int = 8, topn: int | None = None, use_mmr: bool | None = None) -> List[Dict[str, Any]]:
    """
    Embed the query with Ollama and search Chroma by embeddings.
    Query expansion and MMR diversity over top-N candidates; env-configurable; backward compatible.
    Returns a list of hits: { "text": str, "meta": dict, "score": float }
    """
    # Expand query
    expanded_query = expand_query(query)
    # Env defaults
    topn = int(os.getenv("RETR_TOPN", 30)) if topn is None else int(topn)
    use_mmr = bool(int(os.getenv("RETR_USE_MMR", "1"))) if use_mmr is None else use_mmr
    lambda_diversity = float(os.getenv("RETR_MMR_LAMBDA", 0.6))
    # 1) get collection and query embedding
    try:
        col = get_collection()
        qvec = get_embedding(expanded_query)
        # 2) search using query_embeddings (NOT query_texts)
        # Build include_list with correct type
        include_items = ["documents", "metadatas", "distances", "embeddings"]
        if not IncludeEnum:
            raise RuntimeError("Chroma IncludeEnum is required for query; not found.")
        include_list = [IncludeEnum[item] for item in include_items]
        res = col.query(
            query_embeddings=[qvec],
            n_results=max(1, int(topn)),
            include=include_list,
        )
    except Exception:
        return []
    # 3) normalize results defensively
    docs = (res.get("documents") or [[]])[0]
    metas = (res.get("metadatas") or [[]])[0]
    dists = (res.get("distances") or [[]])[0]
    embeds = (res.get("embeddings") or [[]])[0]
    # Defensive: if embeddings missing, compute
    if not embeds or any(e is None or not isinstance(e, list) for e in embeds):
        embeds = [get_embedding(d) for d in docs]
    payloads = []
    for text, meta, dist, emb in zip(docs, metas, dists, embeds):
        d = float(dist) if dist is not None else 1.0
        score = 1.0 / (1.0 + d)
        payloads.append({"text": text or "", "meta": meta or {}, "score": score, "embedding": emb})
    # MMR selection
    if use_mmr:
        mmr_hits = mmr_select(qvec, [p["embedding"] for p in payloads], payloads, k, lambda_diversity)
        # Remove embedding from output for backward compatibility
        return [{"text": h["text"], "meta": h["meta"], "score": h["score"]} for h in mmr_hits]
    # Fallback: sort by Chroma distance
    sorted_hits = sorted(payloads, key=lambda h: 1.0/(1.0+h["score"]), reverse=True)[:k]
    return [{"text": h["text"], "meta": h["meta"], "score": h["score"]} for h in sorted_hits]
