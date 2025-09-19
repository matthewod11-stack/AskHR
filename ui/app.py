# ui/app.py
import os
import time
import requests
import streamlit as st
from urllib.parse import urljoin
from dotenv import load_dotenv

load_dotenv()
API_URL = os.getenv("API_URL", "http://localhost:8000")
DEFAULT_MODEL = os.getenv("LLM_MODEL", "llama3.1:8b")

st.set_page_config(page_title="Ask HR (Local)", layout="centered")
st.title("Ask HR (Local)")

# messages: list of {"role": "user"|"assistant", "content": str, "citations": list[dict]}
if "messages" not in st.session_state:
    st.session_state.messages = []

# ---------------- Sidebar options ----------------
with st.sidebar:
    st.header("Options")
    k = st.slider("Top k results", 4, 12, 8)
    model = st.text_input("Model", DEFAULT_MODEL)
    grounded = st.checkbox("Grounded only", value=False)

    if st.button("Health Check"):
        try:
            resp = requests.get(f"{API_URL}/health", timeout=10)
            resp.raise_for_status()
            st.success(resp.json())
        except Exception as e:
            st.toast(f"Health check failed: {e}", icon="⚠️")


# ---------------- Helpers ----------------
def stream_tokens(text: str, delay: float = 0.002):
    """Client-side visual streaming for a completed answer."""
    for tk in text.split():
        st.write(tk + " ", end="", unsafe_allow_html=True)
        time.sleep(delay)


def norm_url(u: str) -> str:
    """Normalize API-relative URLs to absolute so the browser can open them."""
    if not u:
        return ""
    return urljoin(API_URL, u) if u.startswith("/") else u


def render_citations(citations):
    """Render citation objects: display_name + Open / Download PDF links."""
    if not citations:
        return
    with st.expander("Citations"):
        for c in citations:
            label = c.get("display_name") or c.get("open_url") or "Source"
            open_url = norm_url(c.get("open_url", ""))
            pdf_url = norm_url(c.get("pdf_url", ""))

            parts = []
            if open_url:
                parts.append(f"[Open]({open_url})")
            if pdf_url:
                parts.append(f"[Download PDF]({pdf_url})")

            suffix = " • ".join(parts) if parts else ""
            if suffix:
                st.markdown(f"- **{label}** — {suffix}")
            else:
                st.markdown(f"- **{label}**")


# ---------------- Transcript (input stays at bottom) ----------------
for msg in st.session_state.messages:
    with st.chat_message("user" if msg["role"] == "user" else "assistant"):
        if msg["role"] == "assistant":
            st.markdown(msg.get("content", ""))
            cits = msg.get("citations") or []
            if cits:
                st.markdown("**Sources**")
                for i, c in enumerate(cits, 1):
                    # tolerate either dict or string
                    if isinstance(c, dict):
                        name = (
                            c.get("display_name") or c.get("source_path") or c.get("id") or "Source"
                        )
                        path = c.get("source_path")
                    else:
                        name, path = str(c), None
                    if path:
                        st.markdown(
                            f"{i}. {name}  \n<small><code>{path}</code></small>",
                            unsafe_allow_html=True,
                        )
                    else:
                        st.markdown(f"{i}. {name}")
        else:
            st.markdown(msg.get("content", ""))

# ---------------- Chat input ----------------
prompt = st.chat_input("Ask about your HR corpus…")
if prompt:
    st.session_state.messages.append({"role": "user", "content": prompt})

    try:
        r = requests.post(
            f"{API_URL}/v1/ask",
            json={
                "query": prompt.strip(),
                "k": k,
                "system": None,
                "grounded_only": grounded,
                "model": model,
            },
            timeout=120,
        )
        r.raise_for_status()
        data = r.json()

        answer = data.get("answer", "")
        citations = data.get("citations", [])
        if not isinstance(citations, list):
            citations = []

        st.session_state.messages.append(
            {"role": "assistant", "content": answer, "citations": citations}
        )
        # re-render to keep the newest message in view and stream tokens
        st.rerun()

    except requests.HTTPError as he:
        detail = he.response.text if getattr(he, "response", None) else str(he)
        st.toast(f"API error: {detail}", icon="❌")
    except Exception as e:
        st.toast(f"Request failed: {e}", icon="❌")
