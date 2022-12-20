import streamlit_app
import dashboard
import index
import streamlit as st

pages = {
    "About": index,
    "Recommender System": streamlit_app,
    "Dashboard": dashboard,
}

st.sidebar.title("Navigation")
page = st.sidebar.selectbox("Select your page", tuple(pages.keys()))
pages[page].app()
