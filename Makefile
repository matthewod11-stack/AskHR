# RAG Service Evaluation Harness

.PHONY: eval eval.save eval.sample

EVAL_PY=eval/run_eval.py
EVAL_CASES=eval/cases.csv
API_URL?=http://localhost:8000

eval:
	python $(EVAL_PY) --api-url $(API_URL) --cases $(EVAL_CASES)

eval.save:
	python $(EVAL_PY) --api-url $(API_URL) --cases $(EVAL_CASES) --save

eval.sample:
	python $(EVAL_PY) --api-url $(API_URL) --cases $(EVAL_CASES) --limit 5
