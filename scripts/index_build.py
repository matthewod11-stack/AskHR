#!/usr/bin/env python3
"""
Builds/refreshes the Chroma index from cleaned chunks under data/clean.

Usage:
  python scripts/index_build.py [--reset]

Env:
  DATA_CLEAN   Override input directory (default: ./data/clean)
  CHROMA_DIR   Persisted index directory (default: ./index)
"""
from __future__ import annotations

import argparse
import os
import pathlib
from typing import List, Tuple

import yaml
from dotenv import load_dotenv
from tqdm import tqdm

from app.store import get_collection, reset_collection
from app.embeddings import get_embedding


load_dotenv()

ROOT = pathlib.Path(__file__).resolve().parents[1]
CLEAN_DIR = pathlib.Path(os.getenv("DATA_CLEAN", ROOT / "data/clean"))


def parse_chunk_file(p: pathlib.Path) -> Tuple[str, dict, str]:
    """
    Returns (id, metadata, body)
    Expects YAML frontmatter with at least: chunk_id, source_path, title, pages
    """
    raw = p.read_text(encoding="utf-8")
    if not raw.startswith("---"):
        raise ValueError(f"missing frontmatter: {p}")
    # Split frontmatter and body
    parts = raw.split("\n---\n", 1)
    if len(parts) != 2:
        raise ValueError(f"malformed frontmatter: {p}")
    fm = parts[0].lstrip("-\n")  # drop initial ---
    body = parts[1]
    meta = yaml.safe_load(fm) or {}
    cid = meta.get("chunk_id")
    if not cid:
        raise ValueError(f"no chunk_id in {p}")
    # ensure a few stable metadata keys are present
    meta.setdefault("source_path", str(p))
    meta.setdefault("title", p.stem)
    meta.setdefault("pages", "n/a-n/a")
    return cid, meta, body


def batched(seq, size: int):
    buf = []
    for item in seq:
        buf.append(item)
        if len(buf) >= size:
            yield buf
            buf = []
    if buf:
        yield buf


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--reset", action="store_true", help="drop and recreate the collection")
    args = ap.parse_args()

    col = reset_collection() if args.reset else get_collection()

    # Gather chunk files
    files = sorted(CLEAN_DIR.rglob("*__chunk*.md"))
    if not files:
        print(f"No chunk files found under {CLEAN_DIR}. Run ingesters first.")
        return

    # Prepare records
    ids: List[str] = []
    metas: List[dict] = []
    docs: List[str] = []
    for p in files:
        try:
            cid, meta, body = parse_chunk_file(p)
            ids.append(cid)
            metas.append(meta)
            docs.append(body)
        except Exception as e:
            print(f"[skip] {p}: {e}")

    total = len(ids)

    # Determine which IDs already exist (skip to keep idempotent)
    existing: set[str] = set()
    try:
        # query in manageable batches; Chroma returns only found IDs
        for chunk in batched(ids, 256):
            try:
                got = col.get(ids=chunk, include=["ids"]) or {}
                for cid in (got.get("ids") or []):
                    existing.add(cid)
            except Exception:
                # If get by ids isn't supported, treat as none existing
                existing = set()
                break
    except Exception:
        existing = set()

    pending = [(i, m, d) for i, m, d in zip(ids, metas, docs) if i not in existing]
    already = total - len(pending)
    print(f"Total chunks: {total} | Already indexed: {already} | To add: {len(pending)}")

    if not pending:
        print(f"✅ Done. Collection 'hr_corpus' now has {col.count()} vectors.")
        return

    # Add in batches with embeddings
    added = 0
    for batch in tqdm(list(batched(pending, 32)), desc="indexing", unit="batch"):
        b_ids = [x[0] for x in batch]
        b_metas = [x[1] for x in batch]
        b_docs = [x[2] for x in batch]
        # compute embeddings one-by-one to be resilient to occasional failures
        succ_ids: List[str] = []
        succ_metas: List[dict] = []
        succ_docs: List[str] = []
        succ_vecs: List[List[float]] = []
        for i, m, t in zip(b_ids, b_metas, b_docs):
            try:
                v = get_embedding(t)
            except Exception:
                # Skip this doc if embedding fails
                continue
            succ_ids.append(i)
            succ_metas.append(m)
            succ_docs.append(t)
            succ_vecs.append(v)
        if not succ_ids:
            continue
        try:
            col.add(ids=succ_ids, documents=succ_docs, metadatas=succ_metas, embeddings=succ_vecs)
            added += len(succ_ids)
        except Exception as e:
            print(f"[batch-error] {e}")

    print(f"Added: {added}")
    try:
        print(f"✅ Done. Collection 'hr_corpus' now has {col.count()} vectors.")
    except Exception as e:
        print(f"count error: {e}")


if __name__ == "__main__":
    main()
