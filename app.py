import streamlit as st
from auth import login, require_auth
from controls import CONTROLS
from evidence import generate_evidence

st.set_page_config(
    page_title="Compliance Auditor",
    page_icon="🛡️",
    layout="wide"
)

login()
require_auth()

st.title("🛡️ Compliance Auditor Platform")
st.caption(f"Usuario: {st.session_state['user']} ({st.session_state['role']})")

control = st.selectbox("Control", list(CONTROLS.keys()))
result = st.radio("Resultado", ["Cumple", "Parcial", "No cumple"])
notes = st.text_area("Observaciones")

if st.button("Registrar evaluación"):
    evidence = generate_evidence(control, result)
    st.success("Evaluación registrada")
    st.json(evidence)
