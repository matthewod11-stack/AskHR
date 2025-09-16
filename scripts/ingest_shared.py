#!/usr/bin/env python3
# Retrieval tuning: token-based chunking (~1000, overlap 180) + CLI flags; consistent YAML metadata.
import hashlib
import os
import pathlib
import re
from typing import Iterable, List, Tuple

import argparse
import yaml
try:
    import tiktoken
    _ENC = tiktoken.get_encoding("cl100k_base")
except Exception:
    _ENC = None

def count_tokens(s: str) -> int:
    if _ENC is not None:
        return len(_ENC.encode(s))
    return max(1, len(s) // 4)  # ~4 chars per token fallback

def split_into_chunks(text: str, chunk_tokens: int, overlap_tokens: int) -> list[str]:
    """
    Split text into token-based chunks with overlap. Uses tiktoken if available, else char-based fallback.
    """
    if not text.strip():
        return []
    if _ENC is None:
        win = chunk_tokens * 4
        ov  = overlap_tokens * 4
        step = max(1, win - ov)
        return [text[i:i+win] for i in range(0, len(text), step)]
    toks = _ENC.encode(text)
    chunks, step = [], max(1, chunk_tokens - overlap_tokens)
    for i in range(0, len(toks), step):
        piece = toks[i:i+chunk_tokens]
        if not piece: break
        chunks.append(_ENC.decode(piece))
    return chunks

def add_chunking_args(ap: argparse.ArgumentParser) -> argparse.ArgumentParser:
    ap.add_argument("--chunk-tokens", type=int, default=1000, help="target tokens per chunk")
    ap.add_argument("--overlap-tokens", type=int, default=180, help="overlap tokens between chunks")
    ap.add_argument("--max-files", type=int, default=0, help="limit number of source files (smoke runs)")
    return ap

ROOT = pathlib.Path(__file__).resolve().parents[1]
RAW_DIR = pathlib.Path(os.getenv("DATA_RAW", ROOT / "data/raw"))
CLEAN_DIR = pathlib.Path(os.getenv("DATA_CLEAN", ROOT / "data/clean"))
CLEAN_DIR.mkdir(parents=True, exist_ok=True)

# ---------- utilities ----------
FRONTMATTER_RE = re.compile(r"^---\s*\n.*?\n---\s*\n", re.DOTALL)

def strip_frontmatter(md: str) -> str:
    return re.sub(FRONTMATTER_RE, "", md, count=1)

def normalize_spaces(text: str) -> str:
    text = text.replace("\r", "")
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()

def compute_chunk_id(rel_src: str, idx: int) -> str:
    return hashlib.sha1(f"{rel_src}::{idx}".encode("utf-8")).hexdigest()

def write_chunk_md(src_rel: pathlib.Path, title: str, pages: str, idx: int, body: str) -> None:
    out_base = (CLEAN_DIR / src_rel).with_suffix("")  # strip original extension
    out_base.parent.mkdir(parents=True, exist_ok=True)
    out_path = out_base.parent / f"{out_base.name}__chunk{idx:04d}.md"
    front = {
        "source_path": str(src_rel),
        "pages": pages,
        "chunk_id": compute_chunk_id(str(src_rel), idx),
        "title": title,
    }
    out_path.write_text(f"---\n{yaml.safe_dump(front, sort_keys=False)}---\n{body}\n", encoding="utf-8")

