import streamlit as st

def sidebar():
    with st.sidebar:
        st.page_link("cards_games_app.py", label="Home", icon="🏠")
        st.page_link("pages/01_High_and_Low.py", label="High and Low", icon="🪙")
        st.page_link("pages/02_Hyakunin_Isshu.py", label="百人一首", icon="🇯🇵")
        st.page_link("pages/03_Links.py", label="Links", icon="🌏")
