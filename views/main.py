from pathlib import Path

import streamlit as st
from PIL import Image

#--- PAGE SET UP ---


#--- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "style" / "main.css"

#--- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | Guillermo Anhuaman"
PAGE_ICON = "🌐"

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON, layout="wide", initial_sidebar_state="collapsed")

#--- LOAD CSS ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)

#--- HERO SECTION ---
st.markdown("<h1 style='text-align: center;'>🌐 Bienvenido! - Welcolme! - ようこそ！ 🌐</h1>", unsafe_allow_html=True)
st.write("### ")

st.markdown("""<p style='text-align: center;'>Selecciona un idioma para continuar</p>
               <p style='text-align: center;'>Select a language to continue</p>
               <p style='text-align: center;'>言語を選択して続行してください</p>
            """, unsafe_allow_html=True)


col1, col2, col3, col4 = st.columns([0.2, 1, 1, 1])
with col1:
    st.write("### ")
with col2:
    col_empty, col_text, col_empty2 = st.columns([1, 2, 1])
    with col_text:
        st.write("### ")
        if st.button("Español"):
            st.switch_page("views/app_esp.py")
with col3:
    col_empty, col_text, col_empty2 = st.columns([1, 2, 1])
    with col_text:
        st.write("### ")
        if st.button("English"):
            st.switch_page("views/app.py")
with col4:
    col_empty, col_text, col_empty2 = st.columns([1, 2, 1])
    with col_text:
        st.write("### ")
        if st.button("日本語"):
            st.switch_page("views/app_jp.py")

            