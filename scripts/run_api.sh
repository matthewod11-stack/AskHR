#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
source "$ROOT/.venv/bin/activate" 2>/dev/null || true
exec uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload

