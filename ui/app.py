
import os, json, requests, textwrap, time
import streamlit as st

API_URL = os.getenv("API_URL","http://localhost:8000").rstrip("/")

st.set_page_config(page_title="Ask HR (Local)", layout="centered")
st.title("Ask HR (Local)")
st.caption("A private HR copilot that answers with receipts.")

with st.sidebar:
    st.subheader("Answer settings")
    k = st.number_input("Top-k sources", min_value=1, max_value=20, value=8, step=1, help="How many chunks to retrieve before composing the answer.")
    grounded_only = st.checkbox("Grounded only", value=False, help="If on, answers will only be returned when sources are found. Otherwise, a best-effort answer may be generated with a clear note.")
    st.divider()
    st.subheader("Health")
    colh1, colh2 = st.columns(2)
    with colh1:
        if st.button("Check API"):
            try:
                r = requests.get(f"{API_URL}/health", timeout=5)
                st.write(r.json())
            except Exception as e:
                st.error(f"/health failed: {e}")
    with colh2:
        if st.button("Check Ollama"):
            try:
                r = requests.get(f"{API_URL}/health/ollama", timeout=5)
                st.write(r.json())
            except Exception as e:
                st.error(f"/health/ollama failed: {e}")
    st.caption("Tip: Use `make ingest.update` when you add docs. Startup never re-embeds; indexing is persistent & incremental.")

st.write("Ask anything about HR:")
query = st.text_area(
    "Question",
    value="",
    height=120,
    placeholder="Examples: “What are the key steps in our PIP?”, “Draft a 30/60/90 for a new backend engineer”, “How does PTO accrue?”",
    label_visibility="collapsed",
    key="qa_query",
)

colq1, colq2 = st.columns([1,1])
with colq1:
    ask_clicked = st.button("Ask", type="primary")
with colq2:
    clear_clicked = st.button("Clear")

if clear_clicked:
    st.experimental_rerun()

if not query.strip():
    st.info("Enter a question and click **Ask**. Enable **Grounded only** to require sources.", icon="💡")

def ask_api(payload: dict) -> dict:
    try:
        r = requests.post(f"{API_URL}/v1/ask", json=payload, timeout=90)
        if r.headers.get("content-type","").startswith("application/json"):
            data = r.json()
            rid_hdr = r.headers.get("X-Request-ID")
            if rid_hdr and not data.get("request_id"):
                data["request_id"] = rid_hdr
            return data
        return {"error": f"Non-JSON response: {r.status_code}", "answer": "", "citations": []}
    except Exception as e:
        return {"error": str(e), "answer": "", "citations": []}

if ask_clicked and query.strip():
    payload = {"query": query.strip(), "k": int(k), "grounded_only": bool(grounded_only)}
    with st.spinner("Retrieving sources and composing answer…"):
        t0 = time.time()
        data = ask_api(payload)
        elapsed = time.time() - t0

    req_id = data.get("request_id") or "n/a"
    err = (data.get("error") or "").strip()
    answer = (data.get("answer") or "").strip()
    citations = data.get("citations") or []
    ungrounded = bool(data.get("ungrounded"))

    if err:
        st.error(f"AskHR could not answer: {err}\n\n`request_id: {req_id}`")
    else:
        st.success("Answer ready.")
        if ungrounded:
            st.warning("This answer may be ungrounded (no matching sources).", icon="⚠️")
        if answer:
            st.markdown(answer)

        if citations:
            st.divider()
            st.caption("Citations")
            for i, c in enumerate(citations, 1):
                path = c.get("source_path") if isinstance(c, dict) else str(c)
                url = f"{API_URL}/v1/file?path={path}"
                st.markdown(f"[{i}] {path}  \n{url}")

        if answer:
            md_lines = [answer, ""]
            if citations:
                md_lines.append("## Sources")
                for i, c in enumerate(citations, 1):
                    path = c.get("source_path") if isinstance(c, dict) else str(c)
                    url = f"{API_URL}/v1/file?path={path}"
                    md_lines.append(f"[{i}] {path}\n{url}")
            md_content = "\n\n".join(md_lines)
            st.download_button("Download Answer (.md)", md_content, file_name="askhr_answer.md", mime="text/markdown")

        st.caption(f"request_id: {req_id} • latency: {elapsed:.2f}s")

    with st.expander("Debug (request/response)"):
        st.code(json.dumps(payload, indent=2), language="json")
        st.code(json.dumps(data, indent=2), language="json")
