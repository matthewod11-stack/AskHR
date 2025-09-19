from pathlib import Path
import importlib
import pytest


def write(p: Path, content: str):
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(content, encoding="utf-8")


@pytest.fixture()
def temp_data_dirs(tmp_path, monkeypatch):
    raw = tmp_path / "raw_root"
    clean = tmp_path / "clean_root"
    raw.mkdir()
    clean.mkdir()
    monkeypatch.setenv("DATA_RAW_DIR", str(raw))
    monkeypatch.setenv("DATA_CLEAN_DIR", str(clean))
    return raw, clean


def test_normalize_and_file_endpoint(temp_data_dirs):
    raw, clean = temp_data_dirs

    # Create a file in raw and a different file in clean
    raw_file_rel = Path("handbook/performance.md")
    clean_file_rel = Path("chunks/handbook/performance.md")

    write(raw / raw_file_rel, "# PIP Policy\n- 30 to 60 days\n")
    write(clean / clean_file_rel, "Chunked content here\n")

    # Reload app modules with new env
    app_module = importlib.import_module("app.main")
    importlib.reload(app_module)
    from app.paths import normalize_source_path

    # Normalizer resolves raw-relative
    resolved, anchor = normalize_source_path(str(raw_file_rel))
    assert resolved.exists()
    assert anchor is None

    # Normalizer resolves with explicit clean prefix
    resolved2, anchor2 = normalize_source_path(f"data/clean/{clean_file_rel.as_posix()}#p1-2")
    assert resolved2.exists()
    assert anchor2 == "p1-2"

    # Clean-relative ("chunks/...") resolution
    resolved3, anchor3 = normalize_source_path(clean_file_rel.as_posix())
    assert resolved3.exists()
    assert anchor3 is None

    # Spin up a test client and hit /v1/file for both
    from fastapi.testclient import TestClient

    client = TestClient(app_module.app)

    r1 = client.get("/v1/file", params={"path": raw_file_rel.as_posix()})
    assert r1.status_code == 200
    assert "PIP Policy" in r1.text

    r2 = client.get("/v1/file", params={"path": f"data/clean/{clean_file_rel.as_posix()}#p1-2"})
    assert r2.status_code == 200
    assert "Chunked content here" in r2.text


def test_traversal_blocked(temp_data_dirs):
    raw, clean = temp_data_dirs
    # Create a harmless file outside the roots
    outside = raw.parent / "outside.txt"
    outside.write_text("nope", encoding="utf-8")

    from app.paths import PathResolutionError, normalize_source_path

    with pytest.raises(PathResolutionError):
        normalize_source_path("../outside.txt")
