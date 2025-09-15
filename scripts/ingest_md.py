# scripts/ingest_md.py
import os, re, pathlib
from typing import Iterable
from dotenv import load_dotenv

load_dotenv()

ROOT = pathlib.Path(__file__).resolve().parents[1]
SRC  = pathlib.Path(os.getenv("DATA_MD_SRC", ROOT / "data/raw"))
OUT  = pathlib.Path(os.getenv("DATA_CLEAN", ROOT / "data/clean"))
OUT.mkdir(parents=True, exist_ok=True)

# tune these if needed
CHUNK_WORDS = 1500
OVERLAP = 200

FRONTMATTER_RE = re.compile(r"^---\s*\n.*?\n---\s*\n", re.DOTALL)

def strip_frontmatter(md: str) -> str:
    return re.sub(FRONTMATTER_RE, "", md, count=1)

def normalize_spaces(text: str) -> str:
    # collapse excessive whitespace but keep newlines modestly
    # (preserve some structure for headings/lists)
    text = text.replace("\r", "")
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()

def split_by_headings(md: str) -> list[str]:
    """
    Prefer splitting at Markdown headings to keep sections coherent.
    """
    parts = re.split(r"(?m)^(?=#)", md)  # split where a line starts with '#'
    # ensure each starts at a heading; if no headings, return as single part
    parts = [p.strip() for p in parts if p.strip()]
    return parts if parts else [md]

def chunk_words(text: str, size: int = CHUNK_WORDS, overlap: int = OVERLAP) -> Iterable[str]:
    words = text.split()
    if not words:
        return []
    step = max(1, size - overlap)
    out = []
    for i in range(0, len(words), step):
        out.append(" ".join(words[i:i + size]))
    return out

def write_chunks(src_path: pathlib.Path, chunks: list[str]):
    rel = src_path.relative_to(SRC)
    base = (OUT / rel).with_suffix("")  # drop .md
    base.parent.mkdir(parents=True, exist_ok=True)
    for idx, part in enumerate(chunks):
        out = base.parent / f"{base.name}__chunk{idx:04d}.md"
        out.write_text(part, encoding="utf-8")

def process_md(md_path: pathlib.Path):
    try:
        raw = md_path.read_text(encoding="utf-8", errors="ignore")
        raw = strip_frontmatter(raw)
        norm = normalize_spaces(raw)
        # first, split along headings; then chunk long sections
        sections = split_by_headings(norm)
        chunks = []
        for sec in sections:
            if len(sec.split()) > CHUNK_WORDS:
                chunks.extend(list(chunk_words(sec)))
            else:
                chunks.append(sec)
        if not chunks:
            print(f"[skip-empty] {md_path}")
            return
        write_chunks(md_path, chunks)
        print(f"[ingested-md] {md_path} -> {len(chunks)} chunks")
    except Exception as e:
        print(f"[error] {md_path}: {e}")

def main():
    md_files = [*SRC.rglob("*.md"), *SRC.rglob("*.markdown"), *SRC.rglob("*.txt")]
    if not md_files:
        print(f"No markdown/text files found in {SRC}. Place files there and re-run.")
        return
    for p in md_files:
        process_md(p)

if __name__ == "__main__":
    main()
