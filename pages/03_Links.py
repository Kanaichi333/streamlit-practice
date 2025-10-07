import streamlit as st

import sidebar
sidebar.sidebar()


st.title("Links")

st.subheader("Yokohama National University")
st.page_link("https://www.ynu.ac.jp", label="横浜国立大学 - Initiative for Global Arts & Sciences")

st.subheader("POCLab")
st.page_link("https://poclab-web.github.io/homepage/", label="Physical Organic Chemistry Lab")
