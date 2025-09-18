#!/usr/bin/env bash
set -euo pipefail

echo "== AskHR: one-command launch =="

# 1) Python env
if [ ! -d ".venv" ]; then
  echo "Creating venv..."
  python3 -m venv .venv
fi
source .venv/bin/activate
pip install -q --upgrade pip
pip install -q -r requirements.txt


# 2) Seed sample pack (idempotent)
python scripts/seed_sample_pack.py || true

# 3) Optional: background incremental ingest (fast, only new/changed)
if [ "${RUN_INGEST_ON_START:-false}" = "true" ]; then
  echo "Starting background incremental ingest..."
  (python scripts/ingest_incremental.py update >/tmp/askhr_ingest.log 2>&1 &)
else
  echo "Skipping ingest on start (RUN_INGEST_ON_START=false). Use 'make ingest.update' when you add files."
fi

# 4) Ensure Ollama models
bash scripts/ensure_models.sh

# 5) Start API and UI
export API_URL="${API_URL:-http://localhost:8000}"
export UI_PORT="${UI_PORT:-8501}"

echo
echo "Starting API (FastAPI @ ${API_URL}) and UI (Streamlit @ http://localhost:${UI_PORT}) ..."
# Kill any leftovers
pkill -f "uvicorn app.main:app" >/dev/null 2>&1 || true
pkill -f "streamlit run ui/app.py" >/dev/null 2>&1 || true

# Start API
(uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload & echo $! > .api.pid) &
sleep 1
# Start UI
(streamlit run ui/app.py --server.port "${UI_PORT}" & echo $! > .ui.pid) &

echo
echo "Demo prompts:"
echo "  1) What are the key steps in our Performance Improvement Plan?"
echo "  2) Draft a 30/60/90 plan for a new backend engineer."
echo "  3) How does PTO accrue for full-time employees?"

echo
echo "Health checks:"
echo "  - curl -s ${API_URL}/health | jq ."
echo "  - curl -s ${API_URL}/health/ollama | jq ."
echo
echo "To stop: make stop"
