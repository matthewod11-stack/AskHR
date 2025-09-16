
# Retrieval tuning: token-based chunking (~1000, overlap 180) + CLI flags; consistent YAML metadata.
import os, pathlib, re, argparse
from typing import Iterable
from dotenv import load_dotenv
from scripts.ingest_shared import (
    RAW_DIR as SRC,
    write_chunk_md,
    strip_frontmatter,
    normalize_spaces,
    split_into_chunks,
    add_chunking_args,
)

load_dotenv()

def process_md(md_path: pathlib.Path, args):
    try:
        raw = md_path.read_text(encoding="utf-8", errors="ignore")
        raw = strip_frontmatter(raw)
        norm = normalize_spaces(raw)
        # Minimal normalization, preserve headings
        chunks = split_into_chunks(norm, args.chunk_tokens, args.overlap_tokens)
        if not chunks:
            print(f"[skip-empty] {md_path}")
            return
        rel = md_path.relative_to(SRC)
        title = md_path.stem
        # For MD, use neutral page range "1-1"
        for idx, part in enumerate(chunks, 1):
            write_chunk_md(rel, title, "1-1", idx, part)
        print(f"[ingested-md] {md_path} -> {len(chunks)} chunks")
    except Exception as e:
        print(f"[error] {md_path}: {e}")

def main():
    parser = argparse.ArgumentParser(description="Markdown ingestion with token-based chunking")
    add_chunking_args(parser)
    args = parser.parse_args()
    md_files = []
    for ext in ("*.md", "*.markdown", "*.txt"):
        md_files.extend((SRC).rglob(ext))
    md_files = [p for p in md_files if "__chunk" not in p.name]
    if not md_files:
        print(f"No markdown/text files found in {SRC}. Place files there and re-run.")
        return
    max_files = args.max_files if args.max_files > 0 else len(md_files)
    for p in md_files[:max_files]:
        process_md(p, args)

if __name__ == "__main__":
    main()
