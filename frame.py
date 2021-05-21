import streamlit_app
import dashboard
import streamlit as st

pages = {
        "Recommender System": streamlit_app,
        "Dashboard": dashboard,
    }

st.sidebar.title("Navigation")
page = st.sidebar.radio("Select your page", tuple(pages.keys()))
pages[page].app()
