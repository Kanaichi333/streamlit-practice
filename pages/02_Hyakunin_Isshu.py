import json
from pathlib import Path
import random

import streamlit as st

import sidebar
sidebar.sidebar()


st.title(":streamlit: 百人一首")
st.write("百人一首を暗記しよう")

json1 = Path(__file__).parent.parent / "sample_data" / "hyakunin_isshu_rounds.json"
with open(json1, "r", encoding="utf-8") as f:
    data = json.load(f)

if "course" not in st.session_state:
    st.session_state["course"] = 0
if "i" not in st.session_state:
    st.session_state["i"] = 0
if "finish" not in st.session_state:
    st.session_state["finish"] = 0

def kaishi():
    st.session_state["course"] = 1

def tsugi():
    st.session_state["i"] += 1


if st.session_state["course"] == 0:
    st.subheader("コース選択")
    course = st.radio("100首の中から選んだ数だけランダムで出題されます", (10, 25, 50, 100))

    data["course"] = course
    data["order"] = random.sample(list(range(1, 101)), course)

    st.button("開始", on_click=kaishi, type="primary")


if st.session_state["course"] == 1:
    json2 = Path(__file__).parent.parent / "sample_data" / "yomifuda.json"
    with open(json2, "r", encoding="utf-8") as f:
        yomifuda = json.load(f)
    
    number = data["order"][st.session_state["i"]]
    uta = yomifuda[str(number)]

    with st.container(border=True):
        st.subheader(uta[0][0])
        st.text(uta[1][0])

    dummy_numbers = random.sample(list(set(range(1, 101)) - set(number)), 3)

    choices = [[uta[1][1], 1]]
    for i in range(3):
        choices.append([yomifuda[str(dummy_numbers[i])][1][1], 0])
    choices = random.shuffle(choices)

    if st.button(choices[0][0]):
        if choices[0][1] == 1:
            seikai

    



    if st.session_state["i"] == data["course"] - 1:
        st.session_state["finish"] == 1



if st.session_state["finish"] == 1:
    st.subheader("お疲れ様でした")




with open(json1, "w") as f:
    json.dump(data, f, indent=4)
