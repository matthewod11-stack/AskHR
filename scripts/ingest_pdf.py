
#!/usr/bin/env python3
# Retrieval tuning: token-based chunking (~1000, overlap 180) + CLI flags; consistent YAML metadata.
# Reminder: Run this script with 'python -m scripts.ingest_pdf' instead of running directly.
import argparse
import os
import pathlib
import re
from typing import List, Tuple
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
    if end is None: end = start
    return str(start), str(end)



def map_chunks_to_pages(texts, chunk_bodies):
    # Map chunk boundaries to page spans by accumulating char count per page
    page_spans = []
    char_accum = 0
    page_boundaries = []
    page_starts = []
    curr_page = 1
    # Build a list of (start_char, end_char, page_num)
    for i, t in enumerate(texts):
        page_starts.append(char_accum)
        char_accum += len(t)
    page_starts.append(char_accum)
    # For each chunk, estimate start/end page
    chunk_spans = []
    curr_idx = 0
    for chunk in chunk_bodies:
        chunk_start = curr_idx
        chunk_end = curr_idx + len(chunk)
        # Find page indices
        start_page = end_page = 1
        for i in range(len(page_starts)-1):
            if chunk_start >= page_starts[i] and chunk_start < page_starts[i+1]:
                start_page = i+1
            if chunk_end > page_starts[i] and chunk_end <= page_starts[i+1]:
                end_page = i+1
        chunk_spans.append((start_page, end_page))
        curr_idx += len(chunk)
    return chunk_spans

def ingest_file(path: pathlib.Path, args):
    rel = path.relative_to(RAW_DIR)
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
        except:
            s_i, e_i = 1, 1
        page_numbers.append((s_i, e_i))
    text = normalize_spaces("\n\n".join(texts))
    if not text.strip():
        print(f"[skip-empty] {rel}")
        return
    chunks = split_into_chunks(text, args.chunk_tokens, args.overlap_tokens)
    # Map chunk boundaries to page spans (approximate)
    char_accum = 0
    page_starts = [0]
    page_map = []
    for i, t in enumerate(texts):
        char_accum += len(t)
        page_starts.append(char_accum)
        page_map.append(page_numbers[i])
    for idx, part in enumerate(chunks, 1):
        # Estimate start/end page for chunk
        chunk_start = sum(len(c) for c in chunks[:idx-1])
        chunk_end = chunk_start + len(part)
        start_page = end_page = 1
        for i in range(len(page_starts)-1):
            if chunk_start >= page_starts[i] and chunk_start < page_starts[i+1]:
                start_page = page_map[i][0]
            if chunk_end > page_starts[i] and chunk_end <= page_starts[i+1]:
                end_page = page_map[i][1]
        pages = f"{start_page}-{end_page}"
        write_chunk_md(rel, title, pages, idx, part)
    print(f"[ingested-pdf] {rel} -> {len(chunks)} chunks")


def main():
    parser = argparse.ArgumentParser(description="PDF ingestion with token-based chunking")
    add_chunking_args(parser)
    parser.add_argument("--glob", type=str, default=None, help='e.g. "*.pdf"')
    args = parser.parse_args()
    files = []
    if args.glob:
        files = [p for p in RAW_DIR.rglob(args.glob) if p.suffix.lower() in SUPPORTED_EXT and "__chunk" not in p.name]
    else:
        for p in RAW_DIR.rglob("*"):
            if p.is_file() and p.suffix.lower() in SUPPORTED_EXT and "__chunk" not in p.name:
                files.append(p)
    if not files:
        print(f"No PDF/DOCX/HTML files found in {RAW_DIR}")
        return
    max_files = args.max_files if args.max_files > 0 else len(files)
    for f in sorted(files)[:max_files]:
        try:
            ingest_file(f, args)
        except Exception as e:
            print(f"[error] {f.relative_to(RAW_DIR)}: {e}")

if __name__ == "__main__":
    main()
