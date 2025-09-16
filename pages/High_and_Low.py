import random
import streamlit as st


st.title("High and Low Game!")
st.write("High か Low かを当ててください。")

if "current_card" not in st.session_state:
        st.session_state["current_card"] = 0

if "next_card" not in st.session_state:
        st.session_state["next_card"] = 0

if st.button("カードを引く"):
    st.session_state["current_card"] = random.randint(1, 13)
    st.write(f"現在のカード: {st.session_state["current_card"]}")

if st.session_state["current_card"] != 0:
    win = 0
    st.write(f"次のカードは {st.session_state["current_card"]} より")

    st.session_state["next_card"] = random.randint(1, 13)

    if st.button("High"):
        if st.session_state["current_card"] < st.session_state["next_card"]:
            win = 3
        elif st.session_state["current_card"] > st.session_state["next_card"]:
            win = 2
        else:
            win = 1

    if st.button("Low"):
        if st.session_state["current_card"] > st.session_state["next_card"]:
            win = 3
        elif st.session_state["current_card"] < st.session_state["next_card"]:
            win = 2
        else:
            win = 1   

    if win == 3:
        st.write(st.session_state["next_card"])
        st.success("You Win! ")

    elif win == 2:
        st.write(st.session_state["next_card"])
        st.error("You Lose ")

    elif win == 1:
        st.write(st.session_state["next_card"])
        st.info("Draw ")
