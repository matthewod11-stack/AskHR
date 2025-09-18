#!/usr/bin/env bash
set -euo pipefail

#!/usr/bin/env bash
set -euo pipefail
mkdir -p logs
export UVICORN_ACCESS_LOG=0
PORT="${API_PORT:-8000}"
HOST="${API_HOST:-127.0.0.1}"
echo "[run_api] starting uvicorn on ${HOST}:${PORT} (background)"
# Use --host explicitly; detach fully; log to logs/api.log
nohup uvicorn app.main:app --host "${HOST}" --port "${PORT}" --reload > logs/api.log 2>&1 < /dev/null &
PID=$!
echo "${PID}" > logs/api.pid
echo "[run_api] pid ${PID}"

