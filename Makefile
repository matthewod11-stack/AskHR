.PHONY: deps format lint typecheck test qa run.api run.ui ingest.once ingest.update index.snapshot.save index.snapshot.load index.build eval.sample eval.save

deps:
	python -m pip install -U pip
	pip install -e ".[dev]"

format:
	black .

lint:
	ruff check .

typecheck:
	mypy .

test:
	PYTHONPATH=. pytest -q

qa: format lint typecheck test

run.api:
	uvicorn app.main:app --reload

run.ui:
	streamlit run ui/app.py	[ingested-md] data/raw/handbook/performance.md -> 1 chunks
	[ingested-md] data/raw/onboarding/306090.md -> 1 chunks
	[ingested-md] data/raw/policy/discipline.md -> 1 chunks
	[ingested-md] data/raw/policy/pto.md -> 1 chunks
	[ingested-md] data/raw/templates/offer_letter.md -> 1 chunks
	[summary] ingested=5 skipped=0	KeyError: "Attempt to overwrite 'module' in LogRecord"

ingest.once:
	python scripts/ingest_run.py --mode once --docs-dir data/raw --manifest index/manifest.json

ingest.update:
	python scripts/ingest_run.py --mode update --docs-dir data/raw --manifest index/manifest.json

# Tar the Chroma persist dir for portable bootstrap
index.snapshot.save:
	mkdir -p snapshots
 
.PHONY: api.smoke
	PYTHONPATH=. pytest -q tests/test_api_smoke.py
	tar -czf snapshots/chroma_$$(/bin/date +%Y%m%d-%H%M).tgz -C index persist manifest.json || true

# Load the most recent snapshot (override with SNAP path if provided)
index.snapshot.load:
	@ls -1t snapshots/chroma_*.tgz | head -n1 > /tmp/_snap || true
	@if [ -n "$$(cat /tmp/_snap 2>/dev/null)" ]; then \
	  tar -xzf $$(cat /tmp/_snap) -C index ; \
	  echo "Restored $$(cat /tmp/_snap)"; \
	else \
	  echo "No snapshot found in ./snapshots"; exit 1; \
	fi

index.build:
	python scripts/index_build.py

eval.sample:
	python -m eval.run_eval --api-url http://localhost:8000 --cases eval/cases.csv --limit 5

eval.save:
	python -m eval.run_eval --api-url http://localhost:8000 --cases eval/cases.csv --save
