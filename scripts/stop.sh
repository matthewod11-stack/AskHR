#!/usr/bin/env bash
set -e
echo "[stop] killing uvicorn/streamlit if running"
pkill -f "uvicorn app.main:app" || true
pkill -f "streamlit run ui/app.py" || true
rm -f logs/api.pid logs/ui.pid || true
echo "[stop] done"
