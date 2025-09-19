# Ask HR (Local)

## Quick Start for Contributors

**Requirements:** Python 3.11, virtualenv recommended.

```sh
python3.11 -m venv .venv
source .venv/bin/activate
make deps && make qa
```

**Common commands:**

- `make deps` — install all dependencies (dev included)
- `make qa` — run format, lint, typecheck, and tests
- `make test` — run unit tests only

**Guardrails:**

- Tests enforce persona inclusion ("Chief People Officer") in prompts
- Tests enforce relative import for `CaseRow` in `eval/utils.py`
- Packaging/import tests for `app.config` and `pydantic_settings`

See `.github/workflows/ci.yml` for CI details. All PRs must pass QA and guardrail tests.

## Overview

Ask HR (Local) is a local-first retrieval and Q&A stack for HR documents. It lets you ingest your own HR content, build a vector index, and query it through a simple web UI — all without relying on external APIs.

The stack is built from:

FastAPI – backend service (retrieval + question answering).

Streamlit – lightweight web UI.

Ollama – local LLM serving chat and embeddings.

Chroma – persistent vector database.

Features

✅ Local ingestion: Convert Markdown, PDF, DOCX, or HTML files into clean, chunked .md with YAML metadata.
✅ Indexing: Embed chunks and store them in Chroma for retrieval.
✅ Grounded answers: Top-k retrieved chunks are injected into the LLM prompt for truly sourced responses.
✅ Grounded only mode: Optionally require answers to be based on sources (no sources, no answer).
✅ Search & Ask: Query your HR corpus via REST or Streamlit UI.
✅ Citations: Answers are returned with links back to the underlying files.
✅ Persona: Responses adopt a pragmatic “Chief People Officer” voice for HR guidance.
✅ Optional session memory: Enable multi-turn context with `ENABLE_DIALOG_MEMORY=true` and `X-Session-ID` header.
⚠️ Rewrite-debug page is disabled by default (`SHOW_REWRITE_DEBUG=false`).

### Session Memory (optional)

- To enable multi-turn context, set `ENABLE_DIALOG_MEMORY=true` in your `.env`.
- Client must send a unique `X-Session-ID` header for continuity.
- Defaults to disabled for safety; when disabled, each request is stateless.

## Observability

- All API requests and errors are logged as JSON lines with a `request_id` for traceability.
- Errors return structured JSON with `error` and `request_id` fields.
- Request IDs are propagated from the `X-Request-ID` header or generated per request.
- Ollama HTTP calls use a configurable timeout (`OLLAMA_TIMEOUT_SECONDS`, default 30s).

## Evaluation

You can run a local evaluation harness to test the system and record results:

### Quick sample run

make eval.sample    # first 5 cases
make eval.save      # full suite, persisted results

Note: If you see ImportError for relative imports, use:
  python -m eval.run_eval --api-url ...

### How it works

- Each eval case has an `expect_grounded` flag:
  - If true, the answer must include citations to pass.
  - If false, any non-empty answer passes.
- Results are written to `eval/results/` with timestamped filenames.

Artifacts are written to `eval/results/`.

## Configuration

| Variable                | Default | Description                                                      |
|------------------------ |---------|------------------------------------------------------------------|
| ASK_TOP_K               | 8       | Default number of top chunks to inject into LLM prompt           |
| ENABLE_DIALOG_MEMORY    | false   | Enable per-session memory (requires X-Session-ID header)         |
| SHOW_REWRITE_DEBUG      | false   | Show rewrite-debug page in UI                                    |
| OLLAMA_TIMEOUT_SECONDS  | 30      | Timeout for Ollama HTTP calls (seconds)                          |

## Data Flow

1. Place raw files in `data/raw/`.
2. Run `make ingest.md` to clean and chunk documents.
3. Run `make index.build` to embed and index chunks in Chroma.
4. Start API (`make run.api`) and UI (`make run.ui`).
5. Query via UI or `/v1/ask` endpoint.
6. Run evaluation (`make eval.sample` or `make eval.save`).

Quick Start
Requirements

Python 3.11+
Ollama
 installed locally
Chroma (bundled as Python dependency)

Setup
git clone <https://github.com/matthewod11-stack/AskHR.git>
cd hr-ask-local
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

Copy the environment template:
cp .env.example .env
Ingest & Index
Add HR docs to data/raw/
python scripts/ingest_md.py data/raw
python scripts/index_build.py
Run API
uvicorn app.main:app --reload

API will run on <http://127.0.0.1:8000>

Run UI
streamlit run ui/app.py
UI will run on <http://localhost:8501>

API Endpoints
POST /v1/ask – Ask a question. Returns {answer, citations}.
POST /v1/search – Retrieve raw chunks from Chroma.
GET /v1/file/{path} – Serve a file from data/raw/.
GET /health – Health check.

## File Serving & Citations

Citations now resolve through a single endpoint:

GET /v1/file?path=<relative-or-prefixed-path[#anchor]>

Paths may be relative to `DATA_RAW_DIR` or `DATA_CLEAN_DIR`, or explicitly prefixed with
`data/raw/...` or `data/clean/...`. Configure roots via `.env` (see `.env.example`).

Example:

```bash
curl -s "http://localhost:8000/v1/file?path=handbook/performance.md"
curl -s "http://localhost:8000/v1/file?path=data/clean/chunks/handbook/performance.md#p1-2"
```

Anchors are accepted and preserved client-side, but the server returns plain text content.

## Ingestion Lifecycle & Snapshots

**First run:**

make ingest.once

**Update after changing docs:**

make ingest.update

**Snapshots:**

make index.snapshot.save
make index.snapshot.load

- Manifest lives at `index/manifest.json`.
- Chunks include `doc_uid` and `file_sha256` in their metadata.
- First run ingests all files and writes the manifest.
- Subsequent runs skip unchanged files for fast incremental updates.
- Deleting a doc and running `make ingest.update` purges its chunks from Chroma.
- Snapshots allow fast backup/restore of the Chroma index and manifest.

Known Issues / To-Dos
Grounded answers: Retrieved text not passed into LLM prompt yet.

UI drift: “Grounded only” toggle and /v1/rewrite-debug endpoint unimplemented.
Eval harness: eval/run_eval.py fails due to missing symbols (EvalCase, etc.).
Error handling: /v1/search swallows exceptions silently.
Mutable state: Conversation memory and citation defaults risk leaking across requests.
Docs mismatch: README previously referenced non-existent logs/, bootstrap.sh, etc.
Contributing
This repo is a work in progress. Contributions are welcome, especially in:
Grounding retrieved text into prompts.
Fixing schema mismatches in eval/.
Improving logging/observability.
Updating unit tests to reflect current behavior.
