#!/usr/bin/env python3
# Retrieval tuning: token-based chunking (~1000, overlap 180) + CLI flags; consistent YAML metadata.
# Reminder: Run this script with 'python -m scripts.ingest_pdf' instead of running directly.

import argparse
import pathlib
import os
from bisect import bisect_right
from typing import Tuple
from dotenv import load_dotenv
from unstructured.partition.auto import partition
from scripts.ingest_shared import (
    RAW_DIR,
    write_chunk_md,
    normalize_spaces,
    split_into_chunks,
    add_chunking_args,
)

load_dotenv()

SUPPORTED_EXT = {".pdf", ".docx", ".doc", ".html", ".htm"}


def element_pages(meta) -> Tuple[str, str]:
    if meta is None:
        return "n/a", "n/a"
    start = getattr(meta, "page_number", None)
    end = getattr(meta, "page_number_end", None)
    if start is None and end is None:
        return "n/a", "n/a"
    if end is None:
        end = start
    return str(start), str(end)


# --- PDF page span helpers ---
def _char_to_page(pos: int, page_starts: list[int]) -> int:
    # Returns 1-based page number. page_starts[0] must be 0.
    return max(1, min(len(page_starts), bisect_right(page_starts, pos)))


def _span_to_pages(start: int, end: int, page_starts: list[int]) -> tuple[int, int]:
    if end <= start:
        end = start + 1
    sp = _char_to_page(start, page_starts)
    ep = _char_to_page(end - 1, page_starts)
    return sp, ep


def ingest_file(path: pathlib.Path, args):
    rel = os.path.relpath(str(path), args.docs_dir)
    title = path.stem
    elements = partition(filename=str(path))
    texts = []
    page_numbers = []
    for el in elements:
        t = getattr(el, "text", None) or str(el)
        if not t:
            continue
        texts.append(t)
        s, e = element_pages(getattr(el, "metadata", None))
        try:
            s_i, e_i = int(s), int(e)
        except Exception:
            s_i, e_i = 1, 1
        page_numbers.append((s_i, e_i))
    text = normalize_spaces("\n\n".join(texts))
    if not text.strip():
        print(f"[skip-empty] {rel}")
        return
    chunks = split_into_chunks(text, args.chunk_tokens, args.overlap_tokens)
    page_starts: list[int] = []
    char_accum = 0
    for t in texts:
        page_starts.append(char_accum)
        char_accum += len(t)
    page_starts.append(char_accum)
    sha = (
        args.manifest_entry.sha256
        if hasattr(args, "manifest_entry") and args.manifest_entry
        else ""
    )
    from app.ingest_manifest import doc_uid_for

    doc_uid = doc_uid_for(str(path), sha)
    for idx, part in enumerate(chunks, 1):
        chunk_start = sum(len(c) for c in chunks[: idx - 1])
        chunk_end = chunk_start + len(part)
        sp, ep = _span_to_pages(chunk_start, chunk_end, page_starts)
        pages = f"{sp}-{ep}"
        meta = {
            "source_path": rel,
            "file_sha256": sha,
            "doc_uid": doc_uid,
            "chunk_id": f"{rel}__chunk{idx:04d}",
            "title": title,
            "pages": pages,
        }
        write_chunk_md(pathlib.Path(rel), title, pages, idx, part)
    print(f"[ingested-pdf] {rel} -> {len(chunks)} chunks")


def main():
    parser = argparse.ArgumentParser(description="PDF ingestion with manifest and doc_uid support")
    add_chunking_args(parser)
    parser.add_argument("--docs-dir", default="data/raw")
    parser.add_argument("--manifest", default="index/manifest.json")
    parser.add_argument("--mode", choices=["once", "update"], default="once")
    parser.add_argument("--files", nargs="*", default=None)
    args = parser.parse_args()

    from app.ingest_manifest import load_manifest, scan_dir

    docs_dir = args.docs_dir
    manifest = load_manifest(args.manifest)
    files = args.files if args.files else scan_dir(docs_dir, exts=(".pdf",))
    files = [f for f in files if "__chunk" not in os.path.basename(f)]
    ingested, skipped = 0, 0
    for f in files:
        entry = manifest.get(os.path.normpath(f))
        if args.mode == "once" and entry:
            skipped += 1
            print(f"[skipped-unchanged] {f}")
            continue
        args.manifest_entry = entry
        ingest_file(pathlib.Path(f), args)
        ingested += 1
    print(f"[summary] ingested={ingested} skipped={skipped}")


if __name__ == "__main__":
    main()
