from __future__ import annotations
import os, shutil, sys
from pathlib import Path

# Try to drop the collection via app.store, then remove the persist dir and manifest sqlite file.
def main() -> None:
    # 1) Try to drop the existing collection cleanly
    try:
        from app.store import get_client, get_collection_name, get_persist_dir
        client = get_client()
        name = get_collection_name()
        try:
            client.delete_collection(name)
            print(f"[index_reset] deleted collection: {name}")
        except Exception as e:
            print(f"[index_reset] delete_collection warn: {e}")
        persist_dir = Path(get_persist_dir()).resolve()
    except Exception:
        # Fallback if store helpers are not available
        persist_dir = Path(os.getenv("CHROMA_PERSIST_DIR", os.getenv("CHROMA_DIR", "index"))).resolve()
        print("[index_reset] using fallback persist dir:", persist_dir)

    # 2) Remove persist dir (Chroma on-disk data)
    if persist_dir.exists():
        shutil.rmtree(persist_dir, ignore_errors=True)
        print(f"[index_reset] removed persist dir: {persist_dir}")

    # 3) Remove manifest sqlite if present
    # Common path used by index_manifest.py; adjust if your repo differs.
    manifest = persist_dir / "manifest.sqlite"
    if manifest.exists():
        try:
            manifest.unlink()
            print(f"[index_reset] removed manifest: {manifest}")
        except Exception as e:
            print(f"[index_reset] manifest unlink warn: {e}")

    print("[index_reset] done")
if __name__ == "__main__":
    sys.exit(main())