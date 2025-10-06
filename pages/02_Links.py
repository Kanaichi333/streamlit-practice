import streamlit as st


with st.sidebar:
    st.page_link("cards_games_app.py", label="Home", icon="🏠")
    st.page_link("pages/01_High_and_Low.py", label="High and Low", icon="🪙")
    st.page_link("pages/02_Links.py", label="Links", icon="🌏")


st.title("Links")

st.subheader("Yokohama National University")
st.page_link("https://www.ynu.ac.jp", label="横浜国立大学 - Initiative for Global Arts & Sciences")

st.subheader("POCLab")
st.page_link("https://poclab-web.github.io/homepage/", label="Physical Organic Chemistry Lab")
