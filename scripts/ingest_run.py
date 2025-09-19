#!/usr/bin/env python3
import argparse
from app.ingest_manifest import scan_dir, build_manifest, load_manifest, save_manifest, diff
import subprocess, sys, os


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--docs-dir", default="data/raw")
    ap.add_argument("--manifest", default="index/manifest.json")
    ap.add_argument("--mode", choices=["once", "update"], default="once")
    ap.add_argument("--chunk-tokens", type=int, default=1000)
    ap.add_argument("--overlap-tokens", type=int, default=180)
    args = ap.parse_args()

    os.makedirs("index", exist_ok=True)
    paths = scan_dir(args.docs_dir)
    old = load_manifest(args.manifest)
    new = build_manifest(paths)
    added, changed, removed, unchanged = diff(old, new)

    # fan out to specific ingesters by ext
    md = [p for p in added + changed if p.lower().endswith((".md", ".markdown"))]
    pdf = [p for p in added + changed if p.lower().endswith(".pdf")]

    def run(cmd):
        print(">>", " ".join(cmd))
        sys.stdout.flush()
        subprocess.check_call(cmd)

    if md:
        run(
            ["python", "-m", "scripts.ingest_md", "--files"]
            + md
            + [
                "--chunk-tokens",
                str(args.chunk_tokens),
                "--overlap-tokens",
                str(args.overlap_tokens),
                "--docs-dir",
                args.docs_dir,
                "--manifest",
                args.manifest,
                "--mode",
                args.mode,
            ]
        )

    if pdf:
        run(
            ["python", "-m", "scripts.ingest_pdf", "--files"]
            + pdf
            + [
                "--chunk-tokens",
                str(args.chunk_tokens),
                "--overlap-tokens",
                str(args.overlap_tokens),
                "--docs-dir",
                args.docs_dir,
                "--manifest",
                args.manifest,
                "--mode",
                args.mode,
            ]
        )

    # save new manifest (for once and update alike)
    save_manifest(args.manifest, new)

    # if update, trigger purging step (each ingester can also purge; it’s OK if run twice as long as purging is idempotent)
    if args.mode == "update":
        pass


if __name__ == "__main__":
    main()
