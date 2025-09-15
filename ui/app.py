import os
import requests
import streamlit as st
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
API_PORT = os.getenv("API_PORT", "8000")
API_URL = f"http://localhost:{API_PORT}"

st.set_page_config(page_title="Ask HR (Local)", layout="centered")
st.title("Ask HR (Local)")
st.caption("Stack: FastAPI, Ollama, Streamlit, Local RAG")

# Sidebar controls
with st.sidebar:
    st.header("Options")
    k = st.slider("Top k results", 4, 12, 8)
    if st.button("Health Check"):
        try:
            resp = requests.get(f"{API_URL}/health", timeout=10)
            resp.raise_for_status()
            st.success("API healthy!")
        except Exception as e:
            st.error(f"Health check failed: {e}")

# Main chat UI
if "chat" not in st.session_state:
    st.session_state.chat = []

query = st.text_input("Enter your HR question:")
ask = st.button("Ask")

def call_ask(q, k):
    r = requests.post(
        f"{API_URL}/v1/ask",
        json={"query": q, "k": k},
        timeout=60,
    )
    r.raise_for_status()
    return r.json()

if ask and query.strip():
    try:
        data = call_ask(query.strip(), k)
        st.session_state.chat.append(("you", query.strip()))
        st.session_state.chat.append(("ai", data.get("answer", ""), data.get("citations", [])))
    except Exception as e:
        st.error(f"Error: {e}")

# Render chat
for turn in st.session_state.chat:
    role = turn[0]
    if role == "you":
        st.markdown(f"**You:** {turn[1]}")
    else:
        answer = turn[1]
        citations = turn[2] if len(turn) > 2 else []
        st.markdown("**AI:**")
        st.write(answer)
        if citations:
            with st.expander("Citations"):
                for c in citations:
                    st.code(c)