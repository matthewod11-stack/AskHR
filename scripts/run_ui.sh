#!/bin/bash
set -e
# load .env if present
if [ -f .env ]; then export $(grep -v '^#' .env | xargs); fi
PORT=${UI_PORT:-8501}
echo "[HR-Ask] Starting Streamlit UI on $PORT..."
exec streamlit run ui/App.py --server.port $PORT

