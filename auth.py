import streamlit as st

USERS = {
    "admin": {"password": "admin123", "role": "Admin"},
    "auditor": {"password": "audit123", "role": "Auditor"}
}

def login():
    st.sidebar.subheader("🔐 Login")
    username = st.sidebar.text_input("Usuario")
    password = st.sidebar.text_input("Contraseña", type="password")

    if st.sidebar.button("Ingresar"):
        user = USERS.get(username)
        if user and user["password"] == password:
            st.session_state["user"] = username
            st.session_state["role"] = user["role"]
            st.sidebar.success("Acceso concedido")
        else:
            st.sidebar.error("Credenciales inválidas")

def require_auth():
    if "user" not in st.session_state:
        st.stop()
