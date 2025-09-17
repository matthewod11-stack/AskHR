test:
	pytest -q

.PHONY: run.api run.ui ingest.md index.build eval.sample eval.save

run.api:
	uvicorn app.main:app --reload

run.ui:
	streamlit run ui/app.py

ingest.md:
	python scripts/ingest_md.py data/raw

index.build:
	python scripts/index_build.py

eval.sample:
	python eval/run_eval.py --api-url http://127.0.0.1:8000 --cases eval/cases.sample.csv --limit 5

eval.save:
	python eval/run_eval.py --api-url http://127.0.0.1:8000 --cases eval/cases.sample.csv --save
