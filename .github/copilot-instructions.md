# Copilot Instructions for Ask HR (Local)

## Project Overview
This is a local Retrieval-Augmented Generation (RAG) system for HR documents, combining Ollama (LLM), Chroma (vector DB), FastAPI (backend), and Streamlit (UI). The system ingests HR content (Markdown, PDF, DOCX, HTML) into chunked, vectorized form for semantic search and Q&A.

## Architecture & Data Flow
- **Ingestion**: Scripts in `scripts/` (`ingest_md.py`, `ingest_pdf.py`, `ingest_shared.py`) process raw files from `data/raw/` into cleaned, chunked Markdown in `data/clean/`.
- **Indexing**: `scripts/index_build.py` embeds chunks and builds/refreshes the Chroma index in `index/`.
- **Backend**: `app/main.py` exposes FastAPI endpoints for search and Q&A, using `app/retriever.py` (vector search), `app/embeddings.py` (Ollama embedding API), and `app/store.py` (Chroma client).
- **Frontend**: `ui/app.py` is a Streamlit app that interacts with the FastAPI backend via REST.

## Developer Workflows
- **One-click launch**: Use `launch.command` to start Ollama, FastAPI, and Streamlit together. It sets env vars and opens the UI in your browser.
- **Manual dev**:
  - API: `bash scripts/run_api.sh` (reloads on code changes)
  - UI: `bash scripts/run_ui.sh`
- **Ingestion & Indexing**:
  - Run `bash scripts/refresh_all.sh` to ingest all sources and rebuild the index.
  - For custom ingestion, run `python -m scripts.ingest_md` or `python -m scripts.ingest_pdf`.
  - Index build: `python scripts/index_build.py [--reset]`
- **Testing embeddings**: `python scripts/test_embedding.py`

## Conventions & Patterns
- **Environment**: Uses `.env` for config; see `.env.example` for reference.
- **Chunking**: Markdown and other docs are split into ~1500-word chunks with overlap for context.
- **Metadata**: Each chunk has YAML frontmatter with `chunk_id`, `source_path`, `title`, and `pages`.
- **Embeddings**: Uses Ollama's `/api/embeddings` endpoint; model is set via `EMBED_MODEL` env var.
- **Chroma**: Persistent index in `index/`; collection name is `hr_corpus`.
- **Session memory**: Backend keeps minimal conversation history (last 3 Q/A pairs) for context continuity.
- **API endpoints**: See `app/main.py` for `/search`, `/ask`, `/health`, etc.
- **UI**: Streamlit UI allows model selection, top-k tuning, and health checks.

## Integration Points
- **Ollama**: LLM and embedding API (default: `http://localhost:11434`).
- **Chroma**: Vector DB for semantic search.
- **FastAPI**: REST API for search/Q&A.
- **Streamlit**: User-facing UI.

## Key Files & Directories
- `app/`: Backend logic (API, retrieval, embeddings, store, schemas)
- `ui/app.py`: Streamlit UI
- `scripts/`: Ingestion, indexing, and utility scripts
- `data/raw/`, `data/clean/`: Source and processed document chunks
- `index/`: Chroma DB files
- `launch.command`: Unified launcher

## Example: Adding New Data
1. Place new files in `data/raw/`.
2. Run `bash scripts/refresh_all.sh`.
3. Verify chunks in `data/clean/` and index in `index/`.

## Example: Debugging API
- Use Streamlit sidebar "Health Check" or call `/health` endpoint directly.
- Check logs in `logs/` for API, Ollama, and UI output.

---
_If any section is unclear or missing, please provide feedback for further refinement._
