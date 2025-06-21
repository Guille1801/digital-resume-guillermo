import streamlit as st

#--- PAGE SET UP ---
main_page = st.Page(
    page = "views/main.py",
    title = "Main Menu",
    icon = "🌐",
    default= True,
)

en_version = st.Page(
    page = "views/app.py",
    title = "English CV",
    icon = "🇺🇸",
)

es_version = st.Page(
    page = "views/app_esp.py",
    title = "CV en Español",
    icon = "🇪🇸",
)

jp_version = st.Page(
    page = "views/app_jp.py",
    title = "日本語の履歴書",
    icon = "🇯🇵",
)

#--- NAVIGATION SETTINGS ---
pg = st.navigation(pages=[main_page, en_version, es_version, jp_version])

#--- RUN NAVIGATION ---
pg.run()