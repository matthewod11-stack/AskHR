from __future__ import annotations

import os
import hashlib
from pathlib import Path
from typing import List, Dict, Any, Union
from datetime import datetime
from importlib import import_module

from scripts.index_manifest import connect, get, upsert
from app.store import get_collection, persist

# ---------- Config ----------
RAW_DIR = Path(os.getenv("DATA_RAW_DIR", "data/raw")).resolve()
EMBED_MODEL = os.getenv("OLLAMA_EMBED_MODEL", "nomic-embed-text")
CHUNK_VERSION = os.getenv("CHUNK_VERSION", "v1")

Primitive = Union[str, int, float, bool]

# ---------- Embedding helpers ----------
def _vectorize_texts(texts: List[str]) -> List[List[float]]:
    """
    Use app.embeddings.embed_texts if available, otherwise fall back to per-item embed_text.
    Ensures embeddings are computed explicitly with the same model used at query time.
    """
    try:
        from app.embeddings import embed_texts  # type: ignore
        return embed_texts(texts)  # type: ignore
    except Exception:
        from app.embeddings import embed_text  # type: ignore
        return [embed_text(t) for t in texts]  # type: ignore

# ---------- Chunking ----------
def _default_chunk_markdown(text: str, max_tokens: int = 1000, overlap: int = 180) -> List[str]:
    """Very simple whitespace chunker as a fallback."""
    words = text.split()
    if max_tokens <= 0:
        return [text]
    step = max(1, max_tokens - max(0, overlap))
    return [" ".join(words[i : i + max_tokens]) for i in range(0, len(words), step)]

def compute_sha256_bytes(b: bytes) -> str:
    h = hashlib.sha256()
    h.update(b)
    return h.hexdigest()

def read_file_bytes(p: Path) -> bytes:
    return p.read_bytes()

def make_chunks(p: Path) -> List[str]:
    max_tokens = int(os.getenv("CHUNK_TOKENS", "1000"))
    overlap = int(os.getenv("OVERLAP_TOKENS", "180"))
    if p.suffix.lower() in {".md", ".txt"}:
        try:
            shared = import_module("scripts.ingest_shared")
            text = p.read_text(encoding="utf-8", errors="ignore")
            # type: ignore[attr-defined]
            return shared.chunk_text(text, max_tokens=max_tokens, overlap_tokens=overlap)
        except Exception:
            text = p.read_text(encoding="utf-8", errors="ignore")
            return _default_chunk_markdown(text, max_tokens=max_tokens, overlap=overlap)
    # Placeholder for PDFs/others until a richer cleaner is wired
    return [p.stem]

# ---------- Chroma upsert ----------
def upsert_chunks_into_chroma(file_path: Path, sha: str, chunks: List[str]) -> int:
    if not chunks:
        return 0

    # Compute embeddings explicitly to avoid Chroma auto-embedding (prevents dimension mismatch)
    vectors: List[List[float]] = _vectorize_texts(chunks)

    col = get_collection()
    base = sha[:8]
    ids: List[str] = [f"{base}-{i:04d}" for i in range(len(chunks))]
    metadatas: List[Dict[str, Primitive]] = [
        {
            "source_path": file_path.as_posix(),
            "sha256": sha,
            "chunk_version": CHUNK_VERSION,
            "embed_model": EMBED_MODEL,
            "i": i,
        }
        for i in range(len(chunks))
    ]
    # Chroma expects lists; provide embeddings explicitly.
    col.upsert(ids=ids, documents=list(chunks), embeddings=vectors, metadatas=metadatas)  # type: ignore[arg-type]
    persist()
    return len(chunks)

# ---------- Reindex policy ----------
def should_reindex(record, path: Path, sha: str) -> bool:
    if record is None:
        return True
    r_sha, r_size, r_mtime_ns, r_embed, r_chunk_ver, _ = record
    if r_sha != sha:
        return True
    if r_embed != EMBED_MODEL:
        return True
    if r_chunk_ver != CHUNK_VERSION:
        return True
    if r_size != path.stat().st_size or r_mtime_ns != path.stat().st_mtime_ns:
        return True
    return False

def scan_files(root: Path) -> List[Path]:
    exts = {".md", ".txt", ".pdf"}
    return [p for p in root.rglob("*") if p.is_file() and p.suffix.lower() in exts]

# ---------- Entry point ----------
def main(mode: str = "update"):
    RAW_DIR.mkdir(parents=True, exist_ok=True)
    con = connect()
    files = scan_files(RAW_DIR)
    changed = 0
    skipped = 0
    for p in files:
        try:
            b = read_file_bytes(p)
            sha = compute_sha256_bytes(b)
            rec = get(con, p.as_posix())
            if not should_reindex(rec, p, sha):
                skipped += 1
                continue
            chunks = make_chunks(p)
            n = upsert_chunks_into_chroma(p, sha, chunks)
            upsert(
                con,
                p.as_posix(),
                sha,
                p.stat().st_size,
                p.stat().st_mtime_ns,
                EMBED_MODEL,
                CHUNK_VERSION,
                n,
            )
            changed += 1
        except Exception as e:
            print(f"[ingest_incremental] WARN: {p} -> {e}")
            continue

    print(
        f"[ingest_incremental] files={len(files)} changed={changed} skipped={skipped} "
        f"at {datetime.now().isoformat(timespec='seconds')}"
    )

if __name__ == "__main__":
    import sys
    mode = sys.argv[1] if len(sys.argv) > 1 else "update"
    main(mode)
