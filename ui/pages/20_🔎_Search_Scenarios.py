import os
import streamlit as st

if not os.getenv("SHOW_REWRITE_DEBUG", "false").lower() in ("1","true","yes"):
    st.info("Rewrite debug is disabled. Set SHOW_REWRITE_DEBUG=true to enable.")
    st.stop()
import os
import streamlit as st
import requests

API_URL = os.getenv("API_URL", "http://localhost:8000")
ASKHR_DEBUG = os.getenv("ASKHR_DEBUG", "0") == "1"

SCENARIOS = {
    "Attrition": [
        {"name": "Eng-only follow-up", "last_user": "show attrition by department", "last_assistant": "Attrition is 12% overall. Sales 18%, Eng 10%, Ops 8%.", "new_user": "what about engineers only?"},
        {"name": "Exclude interns / last 90d", "last_user": "show attrition by department", "last_assistant": "Attrition is 12% overall. Sales 18%, Eng 10%, Ops 8%.", "new_user": "last 90 days, exclude interns"},
    ],
    "Headcount": [
        {"name": "Q3 only", "last_user": "show headcount trends for 2023", "last_assistant": "Grew from 60 to 90 employees.", "new_user": "Q3 only"},
        {"name": "By location (incl contractors)", "last_user": "show headcount trends for 2023", "last_assistant": "Grew from 60 to 90 employees.", "new_user": "by location SF, include contractors"},
    ],
    "DEI": [
        {"name": "ICs slice", "last_user": "show DEI metrics for Q2 2024", "last_assistant": "Overall improved female leadership +3%.", "new_user": "just ICs"},
        {"name": "Senior IC vs last quarter", "last_user": "show DEI metrics for Q2 2024", "last_assistant": "Improved leadership +3%.", "new_user": "women in senior IC (L5+) vs last quarter"},
    ],
    "Recruiting": [
        {"name": "Include contractors", "last_user": "open reqs by org and seniority", "last_assistant": "14 total, Eng 8 (3 Sr+), Sales 4 (1 Sr+), Ops 2.", "new_user": "include contractors"},
        {"name": "SR roles H2 only", "last_user": "pipeline health for software engineer roles", "last_assistant": "Pass-through rate 28%, offer-accept 71%.", "new_user": "last 6 months, senior roles only"},
    ],
    "Perf & Comp": [
        {"name": "Compensation linkage", "last_user": "how do performance reviews work?", "last_assistant": "Annual in Q4 with calibration.", "new_user": "and compensation?"},
        {"name": "Engineers only", "last_user": "calibration guidelines", "last_assistant": "Use distribution bands; edge cases via VP approval.", "new_user": "for engineers only"},
    ],
    "Policies": [
        {"name": "Short PIP", "last_user": "PIP policy and template", "last_assistant": "Standard 60-day PIP with weekly checkpoints.", "new_user": "shorter 30-day version?"},
        {"name": "CA hourly PTO", "last_user": "PTO policy overview", "last_assistant": "Unlimited exempt; hourly accrue 1h/30h worked.", "new_user": "California hourly only"},
    ],
    "Edge Cases": [
        {"name": "Standalone (no rewrite)", "last_user": "", "last_assistant": "", "new_user": "show headcount by department and location for 2022–2024 with quarterly granularity"},
        {"name": "SQL guard (no rewrite)", "last_user": "show attrition by department", "last_assistant": "Sales 18%, Eng 10%, Ops 8%.", "new_user": "SELECT dept, COUNT(*) FROM employees WHERE terminated_at >= '2024-01-01';"},
    ]
}

st.set_page_config(page_title="Search Scenarios", layout="wide")
st.title("🔎 Search Scenarios Playground")

st.sidebar.header("Scenario Controls")
group = st.sidebar.selectbox("Scenario Group", list(SCENARIOS.keys()), index=0)
if group is None:
    st.error("Please select a scenario group.")
    st.stop()
scenarios = SCENARIOS[group]
scenario_names = [s["name"] for s in scenarios]
selected_idx = st.sidebar.selectbox("Scenario", range(len(scenarios)), format_func=lambda i: scenario_names[i])
if selected_idx is None:
    st.error("Please select a scenario.")
    st.stop()
selected = scenarios[selected_idx]

use_rewritten = st.sidebar.checkbox("Use rewritten for next Ask", value=True)
k = st.sidebar.number_input("Top-K", min_value=1, max_value=20, value=8)

st.subheader(f"Scenario: {selected['name']}")
col1, col2, col3 = st.columns(3)
col1.markdown(f"**Last User:**\n{selected['last_user']}")
col2.markdown(f"**Last Assistant:**\n{selected['last_assistant']}")
col3.markdown(f"**New Follow-up:**\n{selected['new_user']}")

rewrite_debug_available = False
rewrite_debug_result = None
if st.button("Preview Rewrite"):
    try:
        resp = requests.post(f"{API_URL}/v1/rewrite-debug", json={
            "last_user": selected["last_user"],
            "last_assistant": selected["last_assistant"],
            "new_user": selected["new_user"]
        }, timeout=10)
        if resp.status_code == 200:
            rewrite_debug_available = True
            rewrite_debug_result = resp.json()
        else:
            st.warning("Rewrite debug not available, running raw only.")
    except Exception:
        st.warning("Rewrite debug not available, running raw only.")

if rewrite_debug_result:
    st.markdown("### Rewrite Debug")
    st.json(rewrite_debug_result)
    was_rewritten = rewrite_debug_result.get("was_rewritten", False)
    st.write(f"Was Rewritten: {was_rewritten}")
    st.write(f"Final Persona Prompt: {rewrite_debug_result.get('persona_prompt','')}")
    rewritten_query = rewrite_debug_result.get("rewritten_query", selected["new_user"])
else:
    rewritten_query = selected["new_user"]

if st.button("Run A/B"):
    st.markdown("## A/B Results")
    ab_col1, ab_col2 = st.columns(2)
    # Raw
    raw_resp = requests.post(f"{API_URL}/v1/ask", json={"query": selected["new_user"], "k": k})
    raw_data = raw_resp.json() if raw_resp.status_code == 200 else {"answer": "Error", "citations": []}
    ab_col1.markdown("**Raw Answer:**")
    ab_col1.markdown(raw_data.get("answer", ""))
    ab_col1.markdown("**Citations:**")
    for c in raw_data.get("citations", []):
        ab_col1.write(c)
    # Rewritten
    rewritten_resp = requests.post(f"{API_URL}/v1/ask", json={"query": rewritten_query, "k": k})
    rewritten_data = rewritten_resp.json() if rewritten_resp.status_code == 200 else {"answer": "Error", "citations": []}
    ab_col2.markdown("**Rewritten Answer:**")
    ab_col2.markdown(rewritten_data.get("answer", ""))
    ab_col2.markdown("**Citations:**")
    for c in rewritten_data.get("citations", []):
        ab_col2.write(c)

if st.button("Run All in Group"):
    st.markdown(f"## All Scenarios in {group}")
    for i, scenario in enumerate(scenarios):
        with st.expander(f"{scenario['name']}"):
            try:
                resp = requests.post(f"{API_URL}/v1/rewrite-debug", json={
                    "last_user": scenario["last_user"],
                    "last_assistant": scenario["last_assistant"],
                    "new_user": scenario["new_user"]
                }, timeout=10)
                debug = resp.json() if resp.status_code == 200 else None
            except Exception:
                debug = None
            raw_resp = requests.post(f"{API_URL}/v1/ask", json={"query": scenario["new_user"], "k": k})
            raw_data = raw_resp.json() if raw_resp.status_code == 200 else {"answer": "Error", "citations": []}
            rewritten_query = debug.get("rewritten_query", scenario["new_user"]) if debug else scenario["new_user"]
            rewritten_resp = requests.post(f"{API_URL}/v1/ask", json={"query": rewritten_query, "k": k})
            rewritten_data = rewritten_resp.json() if rewritten_resp.status_code == 200 else {"answer": "Error", "citations": []}
            st.markdown(f"**Raw Input:** {scenario['new_user']}")
            st.markdown(f"**Rewritten Query:** {rewritten_query}")
            st.markdown(f"**Raw Answer:** {raw_data.get('answer','')}")
            st.markdown(f"**Raw Citations:**")
            for c in raw_data.get("citations", []):
                st.write(c)
            st.markdown(f"**Rewritten Answer:** {rewritten_data.get('answer','')}")
            st.markdown(f"**Rewritten Citations:**")
            for c in rewritten_data.get("citations", []):
                st.write(c)
