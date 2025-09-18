from __future__ import annotations
import sqlite3, os, time
from pathlib import Path
from typing import Optional, Tuple

DB_PATH = Path(os.getenv("PERSIST_DIR","index")) / "manifest.db"

SCHEMA = """
CREATE TABLE IF NOT EXISTS files (
  path TEXT PRIMARY KEY,
  sha256 TEXT NOT NULL,
  size INTEGER NOT NULL,
  mtime_ns INTEGER NOT NULL,
  embed_model TEXT NOT NULL,
  chunk_version TEXT NOT NULL,
  chunk_count INTEGER NOT NULL,
  updated_at INTEGER NOT NULL
);
"""

def connect():
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)
    con = sqlite3.connect(str(DB_PATH))
    con.execute(SCHEMA)
    return con

def get(con, path:str) -> Optional[tuple]:
    cur = con.execute("SELECT sha256, size, mtime_ns, embed_model, chunk_version, chunk_count FROM files WHERE path = ?", (path,))
    return cur.fetchone()

def upsert(con, path:str, sha256:str, size:int, mtime_ns:int, embed_model:str, chunk_version:str, chunk_count:int):
    con.execute("""
        INSERT INTO files(path, sha256, size, mtime_ns, embed_model, chunk_version, chunk_count, updated_at)
        VALUES(?,?,?,?,?,?,?,?)
        ON CONFLICT(path) DO UPDATE SET
          sha256=excluded.sha256, size=excluded.size, mtime_ns=excluded.mtime_ns,
          embed_model=excluded.embed_model, chunk_version=excluded.chunk_version,
          chunk_count=excluded.chunk_count, updated_at=excluded.updated_at
    """, (path, sha256, size, mtime_ns, embed_model, chunk_version, chunk_count, int(time.time())))
    con.commit()
