import streamlit as st

# Configuración de la página (estilo NexusAI)
st.set_page_config(page_title="Mi Navegador Web", page_icon="🌐", layout="wide")

# Estilo CSS para que se vea profesional
st.markdown("""
    <style>
    .main {
        background-color: #f0f2f6;
    }
    .stTextInput > div > div > input {
        border-radius: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("🌐 Mi Navegador Personal")
st.markdown("---")

# Barra de búsqueda
url = st.text_input("Introduce la URL (ejemplo: https://www.wikipedia.org)", "https://www.google.com/search?igu=1")

col1, col2, col3 = st.columns([1, 8, 1])

with col2:
    st.info(f"Navegando en: {url}")
    # El truco: Usamos un iframe para mostrar la web
    # Nota: Muchas webs (Google, Facebook) bloquean esto por seguridad (X-Frame-Options)
    st.components.v1.iframe(url, height=600, scrolling=True)

st.sidebar.markdown("### Configuración")
st.sidebar.write("Este es un navegador básico creado con Streamlit.")
if st.sidebar.button("Limpiar Caché"):
    st.rerun()
