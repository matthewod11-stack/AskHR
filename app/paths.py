from __future__ import annotations
from pathlib import Path
from typing import Optional, Tuple
from .config import settings


class PathResolutionError(ValueError):
    pass


RAW_PREFIXES = ("data/raw/", "raw/")
CLEAN_PREFIXES = ("data/clean/", "clean/")


def _strip_anchor(p: str) -> tuple[str, Optional[str]]:
    if "#" in p:
        base, anchor = p.split("#", 1)
        return base, anchor
    return p, None


def _within(root: Path, candidate: Path) -> bool:
    try:
        candidate.relative_to(root)
        return True
    except Exception:
        return False


def normalize_source_path(source_path: str) -> Tuple[Path, Optional[str]]:
    """
    Normalize a citation/source path into a real file under one of the allowed roots.

    Accepts:
      - raw-relative (e.g., "handbook/performance.md")
      - clean-relative (e.g., "chunks/handbook/performance.md")
      - 'data/raw/...'
      - 'data/clean/...'
      - 'raw/...'
      - 'clean/...'

    Returns (resolved_path, anchor) or raises PathResolutionError.
    """
    if not source_path or source_path.strip() == "":
        raise PathResolutionError("Empty source_path")

    base, anchor = _strip_anchor(source_path.strip())
    # normalize slashes & remove leading slashes
    norm = Path(base.lstrip("/")).as_posix()

    # Case 1: explicit raw/clean prefix — strip and join to the correct root
    for pref in RAW_PREFIXES:
        if norm.startswith(pref):
            tail = norm[len(pref) :]
            candidate = (settings.DATA_RAW_DIR / tail).resolve()
            if (
                candidate.exists()
                and candidate.is_file()
                and _within(settings.DATA_RAW_DIR.resolve(), candidate)
            ):
                return candidate, anchor
            raise PathResolutionError(f"Could not resolve path under raw: {source_path}")

    for pref in CLEAN_PREFIXES:
        if norm.startswith(pref):
            tail = norm[len(pref) :]
            candidate = (settings.DATA_CLEAN_DIR / tail).resolve()
            if (
                candidate.exists()
                and candidate.is_file()
                and _within(settings.DATA_CLEAN_DIR.resolve(), candidate)
            ):
                return candidate, anchor
            raise PathResolutionError(f"Could not resolve path under clean: {source_path}")

    # Case 2: unknown prefix — try as raw-relative and clean-relative
    raw_try = (settings.DATA_RAW_DIR / norm).resolve()
    if raw_try.exists() and raw_try.is_file() and _within(settings.DATA_RAW_DIR.resolve(), raw_try):
        return raw_try, anchor

    clean_try = (settings.DATA_CLEAN_DIR / norm).resolve()
    if (
        clean_try.exists()
        and clean_try.is_file()
        and _within(settings.DATA_CLEAN_DIR.resolve(), clean_try)
    ):
        return clean_try, anchor

    raise PathResolutionError(f"Could not resolve path: {source_path}")
