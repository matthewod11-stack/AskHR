#!/bin/bash

# Activate local .venv
source .venv/bin/activate

# Run ingestion scripts
python -m scripts.ingest_md
python -m scripts.ingest_pdf

# Run index build
python scripts/index_build.py

echo "✅ All ingestion and indexing tasks complete!"