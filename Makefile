# -------- AskHR Makefile (stable full replacement) --------
SHELL := /bin/bash

# Defaults (can be overridden: e.g., `make API_PORT=9000 up`)
PYTHON   ?= python
API_HOST ?= 127.0.0.1
API_PORT ?= 8000
UI_PORT  ?= 8501
API_URL   = http://$(API_HOST):$(API_PORT)

.PHONY: up up.nowait down api.run ui.run api.foreground ui.foreground logs.tail logs.check clean.logs health \
        ingest.once ingest.update ingest.md index.reset ingest.rebuild

# --- Orchestration ---
up:
	./scripts/stop.sh || true
	API_HOST=$(API_HOST) API_PORT=$(API_PORT) ./scripts/run_api.sh
	./scripts/wait_for_api.sh $(API_URL)/health http://127.0.0.1:$(API_PORT)/health
	API_URL=$(API_URL) UI_PORT=$(UI_PORT) ./scripts/run_ui.sh
	@echo "Open UI: http://localhost:$(UI_PORT)"

up.nowait:
	./scripts/stop.sh || true
	API_HOST=$(API_HOST) API_PORT=$(API_PORT) ./scripts/run_api.sh
	API_URL=$(API_URL) UI_PORT=$(UI_PORT) ./scripts/run_ui.sh
	@echo "Open UI: http://localhost:$(UI_PORT)"

down:
	./scripts/stop.sh

# --- Individual services ---
api.run:
	API_HOST=$(API_HOST) API_PORT=$(API_PORT) ./scripts/run_api.sh
	./scripts/wait_for_api.sh $(API_URL)/health http://127.0.0.1:$(API_PORT)/health

api.foreground:
	UVICORN_ACCESS_LOG=1 uvicorn app.main:app --host $(API_HOST) --port $(API_PORT) --reload

ui.run:
	API_URL=$(API_URL) UI_PORT=$(UI_PORT) ./scripts/run_ui.sh

ui.foreground:
	API_URL=$(API_URL) streamlit run ui/app.py --server.port $(UI_PORT) --server.headless true

# --- Logs & health ---
logs.tail:
	@echo "---- api.log ----"; tail -n 100 -f logs/api.log & \
	 echo "---- ui.log ----";  tail -n 100 -f logs/ui.log

logs.check:
	@echo "API last lines:"; tail -n 60 logs/api.log || true; \
	 echo ""; echo "UI last lines:"; tail -n 80 logs/ui.log || true

clean.logs:
	mkdir -p logs
	rm -f logs/*.pid || true
	: > logs/api.log || true
	: > logs/ui.log  || true

health:
	curl -sv $(API_URL)/health || true

# --- Ingestion / index ---
ingest.once:
	$(PYTHON) -m scripts.ingest_incremental once

ingest.update:
	$(PYTHON) -m scripts.ingest_incremental update

# Alias to keep compatibility; runs the same incremental update
ingest.md:
	$(MAKE) ingest.update

index.reset:
	$(PYTHON) scripts/index_reset.py

ingest.rebuild: index.reset
	$(PYTHON) -m scripts.ingest_incremental once
