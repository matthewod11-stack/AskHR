#!/usr/bin/env python3
"""
Derive human-friendly display names for sources.
1) If a chunk front-matter includes an H1-derived title, use it.
2) Else call local LLM (Ollama) once per source file to summarize a 6-10 word title.
Writes a mapping to data/display_names.json and can optionally update Chroma metadata.
"""
import os
import json
import pathlib
import re
import httpx
from dotenv import load_dotenv

load_dotenv()
ROOT = pathlib.Path(__file__).resolve().parents[1]
CLEAN = pathlib.Path(os.getenv("DATA_CLEAN", ROOT / "data/clean"))
OLLAMA_URL = os.getenv("OLLAMA_URL", "http://localhost:11434")


def h1_from_markdown(body: str) -> str | None:
    m = re.search(r"^#\s+(.+)$", body, flags=re.MULTILINE)
    return m.group(1).strip() if m else None


def llm_title(text: str) -> str:
    prompt = (
        "Give a concise 6-10 word title for this HR document, no punctuation at end:\n\n"
        + text[:2000]
    )
    with httpx.Client(timeout=30) as c:
        r = c.post(f"{OLLAMA_URL}/api/generate", json={"model": "llama3.1:8b", "prompt": prompt})
        r.raise_for_status()
        return r.json().get("response", "").strip()


def main(update_index: bool = True):
    # Build map from source_path → display_name
    name_map = {}
    # group chunks by their source_path
    groups = {}
    for p in CLEAN.rglob("*.md"):
        txt = p.read_text(encoding="utf-8")
        if txt.startswith("---"):
            fm, body = txt.split("---", 2)[1:]
            # quick and dirty front-matter parse
            src = re.search(r"source_path:\s*(.+)", fm)
            source_path = src.group(1).strip() if src else str(p)
            groups.setdefault(source_path, []).append(body)
    for src, bodies in groups.items():
        # try H1
        title = None
        for b in bodies:
            title = h1_from_markdown(b)
            if title:
                break
        if not title:
            # fallback: LLM title from the first body
            title = llm_title(bodies[0])
        name_map[src] = title

    out = ROOT / "data" / "display_names.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(name_map, indent=2), encoding="utf-8")
    print(f"[names] wrote {out} with {len(name_map)} entries")

    if update_index:
        # col removed (unused)
        # best-effort: update metadatas in place (Chroma python API allows upserts; not all versions support update)
        # We can re-add docs with same IDs but new metadatas; here we only return the map; API will use it to decorate citations.
        print(
            "[names] Skipping direct Chroma updates; the API will decorate citations using display_names.json"
        )


if __name__ == "__main__":
    main()
