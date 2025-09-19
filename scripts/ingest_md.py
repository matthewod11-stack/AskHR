# Retrieval tuning: token-based chunking (~1000, overlap 180) + CLI flags; consistent YAML metadata.
import pathlib
import argparse
import os
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
        chunks = split_into_chunks(norm, args.chunk_tokens, args.overlap_tokens)
        if not chunks:
            print(f"[skip-empty] {md_path}")
            return
        rel = os.path.relpath(str(md_path), args.docs_dir)
        title = md_path.stem
        sha = (
            args.manifest_entry.sha256
            if hasattr(args, "manifest_entry") and args.manifest_entry
            else ""
        )
        from app.ingest_manifest import doc_uid_for

        doc_uid = doc_uid_for(str(md_path), sha)
        for idx, part in enumerate(chunks, 1):
            meta = {
                "source_path": rel,
                "file_sha256": sha,
                "doc_uid": doc_uid,
                "chunk_id": f"{rel}__chunk{idx:04d}",
                "title": title,
                "pages": "1-1",
            }
            write_chunk_md(pathlib.Path(rel), title, "1-1", idx, part)
        print(f"[ingested-md] {md_path} -> {len(chunks)} chunks")
    except Exception as e:
        print(f"[error] {md_path}: {e}")


def main():
    parser = argparse.ArgumentParser(
        description="Markdown ingestion with manifest and doc_uid support"
    )
    add_chunking_args(parser)
    parser.add_argument("--docs-dir", default="data/raw")
    parser.add_argument("--manifest", default="index/manifest.json")
    parser.add_argument("--mode", choices=["once", "update"], default="once")
    parser.add_argument("--files", nargs="*", default=None)
    args = parser.parse_args()

    from app.ingest_manifest import load_manifest, scan_dir

    docs_dir = args.docs_dir
    manifest = load_manifest(args.manifest)
    files = args.files if args.files else scan_dir(docs_dir, exts=(".md", ".markdown"))
    files = [f for f in files if "__chunk" not in os.path.basename(f)]
    ingested, skipped = 0, 0
    for f in files:
        entry = manifest.get(os.path.normpath(f))
        if args.mode == "once" and entry:
            skipped += 1
            print(f"[skipped-unchanged] {f}")
            continue
        args.manifest_entry = entry
        process_md(pathlib.Path(f), args)
        ingested += 1
    print(f"[summary] ingested={ingested} skipped={skipped}")


if __name__ == "__main__":
    main()
