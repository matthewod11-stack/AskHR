# Ask HR (Local)

Your private, local-first HR knowledge assistant.  
Ingest your HR resources (Markdown, PDF, DOCX, HTML), build a searchable index, and chat with your own corpus — all offline.

![Ask HR Screenshot](docs/screenshot_ui.png)

---

## ✨ Features
- 🔒 **Local-first**: Runs entirely on your machine with [Ollama](https://ollama.ai).
- 📚 **Bring your own HR corpus**: Drop HR docs into `data/raw/`.
- 🧩 **Multi-format ingestion**: Markdown, TXT, PDF, DOCX, HTML → clean chunks with metadata.
- 🔎 **Vector search**: Powered by [Chroma](https://www.trychroma.com/).
- 🤖 **Ask anything**: Local RAG + Llama (`llama3.1:8b` default).
- 📑 **Citations**: Every answer includes clickable citations back to the source files.
- 🖥️ **Simple UI**: Streamlit chat app with model selector and grounded-only toggle.
- 🖱️ **One-click launch**: macOS launcher script (`scripts/launch.command`).

---

## 🚀 Quickstart

### 1. Clone & bootstrap
```bash
git clone https://github.com/yourname/hr-ask-local.git
cd hr-ask-local
bash scripts/bootstrap.sh
This will:

Create .venv

Install dependencies

Ensure Ollama models are pulled (llama3.1:8b, nomic-embed-text)

2. Ingest your HR documents
Drop files into data/raw/:

Markdown/TXT → scripts/ingest_md.py

PDF/DOCX/HTML → scripts/ingest_pdf.py

bash
Copy code
source .venv/bin/activate
python scripts/ingest_md.py
python scripts/ingest_pdf.py --glob "*.pdf"
Chunks with YAML frontmatter appear in data/clean/.

3. Build / refresh index
bash
Copy code
python scripts/index_build.py --reset   # first time
python scripts/index_build.py           # append mode
4. Launch everything
bash
Copy code
bash scripts/launch.command
This starts:

Ollama (embeddings + LLM)

FastAPI backend (http://localhost:8000)

Streamlit UI (http://localhost:8501)

Logs are in ./logs/.

5. Ask questions
Open http://localhost:8501 in your browser.

Type a question (“How do I structure a PIP?”)

Watch streaming answers

Expand citations → click through to original sources

🔍 API Usage
Health
bash
Copy code
curl -s http://localhost:8000/health | jq
Search only
bash
Copy code
curl -s -X POST http://localhost:8000/v1/search \
  -H 'content-type: application/json' \
  -d '{"query":"performance improvement plan","k":5}' | jq
Ask (RAG + LLM)
bash
Copy code
curl -s -X POST http://localhost:8000/v1/ask \
  -H 'content-type: application/json' \
  -d '{"query":"help with a low performer","k":8,"grounded_only":true}' | jq
🧪 Evaluation
Benchmark quality with eval harness:

bash
Copy code
python eval/run_eval.py --k 8
Outputs:

Keyword coverage

Citation rate

Results saved to eval/results.jsonl

🛠️ Troubleshooting
Port already in use

bash
Copy code
lsof -i :8000 -i :8501 | awk 'NR>1{print $2}' | xargs -r kill -9
UI spins / no response

Check logs/api.log and logs/ollama.log

Ensure Ollama is running: pgrep ollama || ollama serve

Rebuild index: python scripts/index_build.py --reset

Model not found

bash
Copy code
ollama pull llama3.1:8b
ollama pull nomic-embed-text
📂 Project Structure
bash
Copy code
data/raw/       # drop your HR documents here
data/clean/     # chunked + YAML annotated files
index/          # ChromaDB index
logs/           # API, UI, Ollama logs

scripts/        # ingestion, indexing, launch scripts
app/            # FastAPI app (schemas, retriever, prompting)
ui/             # Streamlit chat UI
eval/           # evaluation harness + cases
docs/           # screenshots, architecture diagrams
🗺️ Roadmap
 Export answers with citations to Markdown/Word

 Add retry + “copy to clipboard” in UI

 Prebuilt macOS app bundle (Ask HR.app)

 Advanced eval metrics (F1, BLEU for HR tasks)

📜 License
MIT (see LICENSE)

🙌 Credits
Built on FastAPI, Streamlit, Chroma, and Ollama.

Persona prompt: Pragmatic, compliance-aware Chief People Officer.
