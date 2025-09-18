import streamlit as st
from ui.kit import ask_api, render_result

st.set_page_config(page_title="30/60/90 Plan Builder — Ask HR", layout="centered")
st.title("30/60/90 Plan Builder")
st.caption("Turn onboarding guidance into a structured 30/60/90 plan with citations.")

with st.sidebar:
    st.subheader("Answer settings")
    k = st.number_input("Top-k sources", min_value=1, max_value=20, value=8, step=1)
    grounded_only = st.checkbox("Grounded only", value=False, help="Require sources to return a draft.")

st.subheader("New hire details")
col1, col2 = st.columns(2)
with col1:
    emp_name = st.text_input("New hire name", "")
    role = st.text_input("Role/Title", "")
with col2:
    manager = st.text_input("Manager", "")
    start_date = st.text_input("Start date (optional)", "")

st.subheader("Focus areas & goals")
focus_areas = st.multiselect("Focus areas", ["Codebase/Tech", "Product/Domain", "Collaboration/Process", "Quality/SRE", "Customer/Support"], default=["Codebase/Tech","Collaboration/Process"])
thirty = st.text_area("30 days — Learn", height=100, placeholder="Environment setup, shadowing, docs, small PRs, pairing...")
sixty = st.text_area("60 days — Contribute", height=100, placeholder="Own a small feature, participate in on-call onboarding, improve test coverage...")
ninety = st.text_area("90 days — Own", height=100, placeholder="Lead a small project, drive a RFC, improve team process...")

metrics = st.text_area("Success metrics (optional)", height=80, placeholder="E.g., 2 PRs/week, 1 feature shipped by day 60, <2 code review iterations, 90% on-time tasks")

if st.button("Generate 30/60/90 Draft", type="primary"):
    areas = ", ".join(focus_areas) if focus_areas else "General"
    q = f"""
Draft a structured 30/60/90 onboarding plan in Markdown for \"{emp_name}\" (role: {role}), manager \"{manager}\", start date \"{start_date}\".

Requirements:
- Sections with headings: Overview, Success Metrics, 30 Days (Learn), 60 Days (Contribute), 90 Days (Own), Stakeholders, Risks & Mitigations.
- Reflect focus areas: {areas}.
- Fold in manager-provided inputs for each phase where present.
- Write in a pragmatic, supportive tone; be specific and outcome-oriented.
- If sources are available, ground process/policy statements with bracketed citations like [1][2]; otherwise note that no sources were found.
- Output should be clean Markdown ready to share.

Manager inputs:
- 30 days: {thirty}
- 60 days: {sixty}
- 90 days: {ninety}
- Success metrics: {metrics}

Deliver only the plan markdown (no preamble).
"""
    data = ask_api(q.strip(), int(k), bool(grounded_only))
    render_result(data)
else:
    st.info("Fill out the form and click **Generate 30/60/90 Draft**. Toggle **Grounded only** to require citations.", icon="🧭")
