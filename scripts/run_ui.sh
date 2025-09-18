#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
source "$ROOT/.venv/bin/activate" 2>/dev/null || true
mkdir -p logs
API_URL="${API_URL:-http://localhost:8000}"
UI_PORT="${UI_PORT:-8501}"
echo "[run_ui] starting streamlit on :${UI_PORT} (background) API_URL=${API_URL}"
nohup env API_URL="${API_URL}" streamlit run ui/app.py --server.port "${UI_PORT}" --server.headless true > logs/ui.log 2>&1 < /dev/null &
PID=$!
echo "${PID}" > logs/ui.pid
echo "[run_ui] pid ${PID}"
