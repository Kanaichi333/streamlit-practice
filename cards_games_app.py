import streamlit as st


with st.sidebar:
    st.page_link("cards_games_app.py", label="Home", icon="🏠")
    st.page_link("pages/High_and_Low.py", label="High and Low", icon="🪙")


st.title("Welcome to Cards Games App!")

st.write("Webアプリ開発の練習として、簡単なカードゲームを実装しています") 
st.write("カードゲームは順次、追加していく予定です。")


with st.container(border=True):
    st.subheader("High and Low")
    st.write("所持金を賭けて High か Low かを当てるゲーム")
    st.write("勝負は3ラウンド")

    st.page_link("pages/High_and_Low.py", label="🔥こちらからプレイ🔥")
