from __future__ import annotations
import hashlib, json, os
from dataclasses import dataclass, asdict
from typing import Dict, List, Tuple


@dataclass
class ManifestEntry:
    path: str
    size: int
    mtime: float
    sha256: str


Manifest = Dict[str, ManifestEntry]  # key = normalized path


def _norm(p: str) -> str:
    return os.path.normpath(p)


def file_sha256(path: str, chunk_size: int = 1 << 20) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        while True:
            b = f.read(chunk_size)
            if not b:
                break
            h.update(b)
    return h.hexdigest()


def scan_dir(docs_dir: str, exts=(".md", ".markdown", ".pdf")) -> List[str]:
    out: List[str] = []
    for root, _, files in os.walk(docs_dir):
        for name in files:
            if name.lower().endswith(exts):
                out.append(_norm(os.path.join(root, name)))
    return sorted(out)


def build_manifest(paths: List[str]) -> Manifest:
    m: Manifest = {}
    for p in paths:
        st = os.stat(p)
        m[_norm(p)] = ManifestEntry(
            path=_norm(p), size=st.st_size, mtime=st.st_mtime, sha256=file_sha256(p)
        )
    return m


def load_manifest(path: str) -> Manifest:
    if not os.path.exists(path):
        return {}
    with open(path, "r", encoding="utf-8") as f:
        raw = json.load(f) or {}
    return {k: ManifestEntry(**v) for k, v in raw.items()}


def save_manifest(path: str, m: Manifest) -> None:
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump({k: asdict(v) for k, v in m.items()}, f, indent=2)


def diff(old: Manifest, new: Manifest) -> Tuple[List[str], List[str], List[str], List[str]]:
    """return (added, changed, removed, unchanged) by path key"""
    added, changed, removed, unchanged = [], [], [], []
    old_keys, new_keys = set(old), set(new)
    for k in sorted(new_keys - old_keys):
        added.append(k)
    for k in sorted(old_keys - new_keys):
        removed.append(k)
    for k in sorted(new_keys & old_keys):
        if old[k].sha256 != new[k].sha256 or old[k].size != new[k].size:
            changed.append(k)
        else:
            unchanged.append(k)
    return added, changed, removed, unchanged


def doc_uid_for(path: str, sha256: str) -> str:
    return f"{_norm(path)}|{sha256[:12]}"
