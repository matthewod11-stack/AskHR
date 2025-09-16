#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
source "$ROOT/.venv/bin/activate" 2>/dev/null || true
exec streamlit run "$ROOT/ui/app.py" --server.port 8501
