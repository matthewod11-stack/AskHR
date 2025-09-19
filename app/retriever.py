#!/usr/bin/env python3
# Retrieval tuning: query expansion + MMR diversity over top-N candidates; env-configurable; backward compatible.
from __future__ import annotations


import os
import pathlib
from app.logging_setup import logger
import math
from typing import Any, Dict, List

from app.store import get_collection
from app.embeddings import get_embedding


# HR synonym expansion
_HR_SYNONYMS = {
    "pip": ["performance improvement plan", "coaching plan", "corrective action"],
    "performance review": ["appraisal", "evaluation", "calibration", "review cycle"],
    "progressive discipline": ["disciplinary action", "written warning", "final warning"],
    "leave": ["pto", "time off", "absence", "fmla"],
    "termination": ["separation", "dismissal", "exit", "involuntary"],
    "onboarding": ["new hire", "orientation", "ramp", "30-60-90", "306090"],
    "compensation": ["pay", "salary", "band", "range", "total rewards"],
    "job description": ["jd", "role profile", "position description"],
}


def expand_query(q: str, max_terms: int = 6) -> str:
    ql = q.lower()
    extras = []
    for k, syns in _HR_SYNONYMS.items():
        if k in ql or any(s in ql for s in syns):
            extras.extend(syns)
    extras = list(dict.fromkeys(extras))[:max_terms]
    return q if not extras else f"{q} :: {' | '.join(extras)}"


def cosine(a, b):
    # Pure python cosine similarity
    if not a or not b or len(a) != len(b):
        return 0.0
    dot = sum(x * y for x, y in zip(a, b))
    norm_a = math.sqrt(sum(x * x for x in a))
    norm_b = math.sqrt(sum(y * y for y in b))
    if norm_a == 0 or norm_b == 0:
        return 0.0
    return dot / (norm_a * norm_b)


def mmr_select(query_vec, cand_vecs, cand_payloads, k, lambda_diversity):
    # Maximal Marginal Relevance selection
    selected, selected_idx = [], set()
    if not cand_vecs:
        return []
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
            if i in selected_idx:
                mmr_scores.append(float("-inf"))
            else:
                sim_to_query = cosine(query_vec, v)
                sim_to_selected = max([cosine(v, cand_vecs[j]) for j in selected_idx], default=0.0)
                mmr_score = (
                    lambda_diversity * sim_to_query - (1 - lambda_diversity) * sim_to_selected
                )
                mmr_scores.append(mmr_score)
        idx = max(range(len(mmr_scores)), key=lambda i: mmr_scores[i])
        selected.append(idx)
        selected_idx.add(idx)
    return [cand_payloads[i] for i in selected]


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


def search_chunks(
    query: str,
    k: int = 8,
    topn: int | None = None,
    use_mmr: bool | None = None,
    min_score: float | None = None,
) -> List[Dict[str, Any]]:
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
    if min_score is None:
        try:
            min_score = float(os.getenv("RETRIEVER_MIN_SCORE", "0.0"))
        except Exception:
            min_score = 0.0
    debug = os.getenv("RETRIEVER_DEBUG", "0") in ("1", "true", "yes")
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
        mmr_hits = mmr_select(
            qvec, [p["embedding"] for p in payloads], payloads, topn, lambda_diversity
        )
        if min_score > 0:
            mmr_hits = [h for h in mmr_hits if h.get("score", 0.0) >= min_score]
        mmr_hits_sorted = sorted(mmr_hits, key=lambda h: h["score"], reverse=True)[:k]
        if debug:
            for h in mmr_hits_sorted[:5]:
                meta = h.get("meta", {})
                logger.info(
                    f"hit score={h.get('score',0.0):.3f} src={meta.get('source_path')} title={meta.get('title')}"
                )
        # Remove embedding from output for backward compatibility
        hits = [
            {"text": h["text"], "meta": h["meta"], "score": h["score"]} for h in mmr_hits_sorted
        ]
    else:
        sorted_hits = sorted(payloads, key=lambda h: h["score"], reverse=True)
        if min_score > 0:
            sorted_hits = [h for h in sorted_hits if h.get("score", 0.0) >= min_score]
        sorted_hits = sorted_hits[:k]
        if debug:
            for h in sorted_hits[:5]:
                meta = h.get("meta", {})
                logger.info(
                    f"hit score={h.get('score',0.0):.3f} src={meta.get('source_path')} title={meta.get('title')}"
                )
        hits = [{"text": h["text"], "meta": h["meta"], "score": h["score"]} for h in sorted_hits]
    # Fallback: keyword scan if enabled and no hits
    if not hits and os.getenv("RETRIEVER_FALLBACK_KEYWORDS", "0") in ("1", "true", "yes"):
        return _keyword_fallback(query, k)
    return hits


def _keyword_fallback(query: str, k: int) -> list[dict]:
    base = os.getenv("DATA_CLEAN", "data/clean")
    terms = [t.strip().lower() for t in query.split() if len(t.strip()) >= 3]
    out: list[dict] = []
    for p in pathlib.Path(base).rglob("*.md"):
        try:
            txt = p.read_text(encoding="utf-8", errors="ignore")
        except Exception:
            continue
        tnorm = txt.lower()
        score = sum(1 for t in terms if t in tnorm)
        if score > 0:
            out.append(
                {
                    "text": txt[:1200],
                    "score": float(score),
                    "meta": {
                        "source_path": str(p).replace("\\", "/"),
                        "title": p.stem.replace("_", " ").title(),
                        "pages": "",
                        "chunk_id": f"kw::{p.name}",
                    },
                }
            )
    out.sort(key=lambda x: x["score"], reverse=True)
    return out[:k]
