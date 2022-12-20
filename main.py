from st_on_hover_tabs import on_hover_tabs
import streamlit_app
import dashboard
import index
import streamlit as st

with st.sidebar:
    tabs = on_hover_tabs(tabName=['About', 'Recommender System', 'Dashboard'], iconName=[
                         'help', 'online_prediction', 'dashboard'],
                         styles={'navtab': {'background-color': '#F0F2F6',
                                            'color': '#31333F',
                                            'font-size': '18px',
                                            'transition': '.3s',
                                            'white-space': 'nowrap',
                                            'text-transform': 'uppercase'},
                                 'tabOptionsStyle': {':hover :hover': {'color': 'red',
                                                                       'cursor': 'pointer'}},
                                 'iconStyle': {'position': 'fixed',
                                               'left': '7.5px',
                                               'text-align': 'left'},
                                 'tabStyle': {'list-style-type': 'none',
                                              'margin-bottom': '30px',
                                              'padding-left': '30px'}},
                         key="1",
                         default_choice=1)
pages = {
    "About": index,
    "Recommender System": streamlit_app,
    "Dashboard": dashboard,
}

if tabs == 'About':
    pages['About'].app()
elif tabs == "Recommender System":
    pages["Recommender System"].app()
elif tabs == "Dashboard":
    pages["Dashboard"].app()
