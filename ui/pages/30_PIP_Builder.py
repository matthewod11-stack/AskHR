import streamlit as st
from ui.kit import ask_api, render_result

st.set_page_config(page_title="PIP Builder — Ask HR", layout="centered")
st.title("PIP Builder")
st.caption("Turn performance concerns into a structured, citation-backed Performance Improvement Plan.")

with st.sidebar:
    st.subheader("Answer settings")
    k = st.number_input("Top-k sources", min_value=1, max_value=20, value=8, step=1)
    grounded_only = st.checkbox("Grounded only", value=False, help="Require sources to return a draft.")

st.subheader("Employee details")
col1, col2 = st.columns(2)
with col1:
    emp_name = st.text_input("Employee name", "")
    role = st.text_input("Role/Title", "")
with col2:
    manager = st.text_input("Manager", "")
    duration = st.selectbox("PIP duration", ["30 days","45 days","60 days"], index=1)

st.subheader("Performance context")
issues = st.text_area("Documented issues (SBI format if possible)", height=120, placeholder="e.g., Missed 3 deadlines in Q2; code review rework; off-sprint work without alignment...")
expectations = st.text_area("SMART expectations/goals", height=120, placeholder="e.g., Deliver feature X by <date>; maintain on-time delivery ≥90%; zero Sev1 bugs introduced...")
support = st.text_area("Support & resources provided", height=100, placeholder="Training, mentor, weekly 1:1 coaching, pairing plan, etc.")
checkins = st.selectbox("Check-in cadence", ["Weekly","Bi-weekly"], index=0)
consequences = st.text_area("Consequences if not met", height=80, placeholder="May lead to further action up to and including termination.")

if st.button("Generate PIP Draft", type="primary"):
    # Compose a structured prompt that the /v1/ask core can ground and cite.
    q = f"""
Draft a formal Performance Improvement Plan (PIP) in Markdown for employee \"{emp_name}\" (role: {role}), managed by \"{manager}\".

Requirements:
- Duration: {duration}. Include a clear start date placeholder and an end date placeholder.
- Structure with headings: Summary, Areas of Concern, SMART Expectations, Timeline & Milestones, Check-ins ({checkins}), Support & Resources, Consequences, Acknowledgement & Signatures.
- Use bullet lists and numbered milestones where appropriate.
- Write in a pragmatic, compliance-aware CPO tone.
- If sources are provided below, ground claims and process steps with bracketed citations like [1][2]; otherwise state that no sources were found.
- Preserve neutrality and avoid legal conclusions.

Inputs (free text provided by manager):
- Areas of concern: {issues}
- SMART expectations: {expectations}
- Support/resources: {support}
- Consequences: {consequences}

Deliver only the PIP markdown body (no preamble). 
"""
    data = ask_api(q.strip(), int(k), bool(grounded_only))
    render_result(data)
else:
    st.info("Fill in the sections and click **Generate PIP Draft**. Toggle **Grounded only** if you require citations.", icon="📝")
