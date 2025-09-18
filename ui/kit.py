import os, json, requests, streamlit as st

API_URL = os.getenv("API_URL","http://localhost:8000").rstrip("/")

def ask_api(query: str, k: int, grounded_only: bool, timeout: int = 90) -> dict:
    try:
        r = requests.post(f"{API_URL}/v1/ask", json={"query": query, "k": int(k), "grounded_only": bool(grounded_only)}, timeout=timeout)
        if r.headers.get("content-type","").startswith("application/json"):
            return r.json()
        return {"error": f"Non-JSON response: {r.status_code}", "answer": "", "citations": []}
    except Exception as e:
        return {"error": str(e), "answer": "", "citations": []}

def render_result(payload: dict):
    req_id = payload.get("request_id") or "n/a"
    err = (payload.get("error") or "").strip()
    ans = (payload.get("answer") or "").strip()
    cits = payload.get("citations") or []
    ungrounded = bool(payload.get("ungrounded"))

    if err:
        st.error(f"Could not generate: {err}\n\n`request_id: {req_id}`")
    else:
        st.success("Draft ready.")
        if ungrounded:
            st.warning("This draft may be ungrounded (no matching sources).", icon="⚠️")
        if ans:
            st.markdown(ans)

        if cits:
            st.divider()
            st.caption("Citations")
            api = API_URL
            for i, c in enumerate(cits, 1):
                if isinstance(c, dict):
                    path = c.get("source_path") or c.get("path") or json.dumps(c)
                else:
                    path = str(c)
                url = f"{api}/v1/file?path={path}"
                st.markdown(f"[{i}] {path}  \n{url}")

        if ans:
            lines = [ans, ""]
            if cits:
                lines.append("## Sources")
                api = API_URL
                for i, c in enumerate(cits, 1):
                    if isinstance(c, dict):
                        path = c.get("source_path") or c.get("path") or json.dumps(c)
                    else:
                        path = str(c)
                    url = f"{api}/v1/file?path={path}"
                    lines.append(f"[{i}] {path}\n{url}")
            md = "\n\n".join(lines)
            st.download_button("Download Draft (.md)", md, file_name="askhr_draft.md", mime="text/markdown")

    with st.expander("Debug (raw payload)"):
        st.code(json.dumps(payload, indent=2), language="json")
