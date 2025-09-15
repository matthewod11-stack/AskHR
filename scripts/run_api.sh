#!/bin/bash
# scripts/run_api.sh
# Start the FastAPI backend for HR Ask Local

set -e

# Load environment variables from .env if present
if [ -f .env ]; then
  export $(grep -v '^#' .env | xargs)
fi

PORT=${API_PORT:-8000}

echo "[HR-Ask] Starting FastAPI server on port $PORT..."
uvicorn app.main:app --reload --port $PORT

