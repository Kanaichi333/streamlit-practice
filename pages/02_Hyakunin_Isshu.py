import json
from pathlib import Path
import random

import streamlit as st

import sidebar
sidebar.sidebar()


st.set_page_config(page_title="百人一首")
st.title(":streamlit: 百人一首")
st.write("百人一首を暗記しよう")

json1 = Path(__file__).parent.parent / "sample_data" / "hyakunin_isshu_rounds.json"
with open(json1, "r", encoding="utf-8") as f:
    data = json.load(f)

if "start" not in st.session_state:
    st.session_state["start"] = 0
if "j" not in st.session_state:
    st.session_state["j"] = 0
if "random" not in st.session_state:
    st.session_state["random"] = 0
if "choose" not in st.session_state:
    st.session_state["choose"] = 0

def start():
    st.session_state["start"] = 1
    st.session_state["j"] = 0
    st.session_state["random"] = 0
    st.session_state["choose"] = 0

def seikai():
    st.session_state["choose"] = 1

def otetsuki():
    st.session_state["choose"] = 2

def next_uta():
    st.session_state["j"] += 1
    st.session_state["random"] = 0
    st.session_state["choose"] = 0

def reset():
    st.session_state["start"] = 0
    st.session_state["j"] = 0
    st.session_state["random"] = 0
    st.session_state["choose"] = 0


if st.session_state["start"] == 0:
    st.subheader("コース選択")
    course = st.radio("100首の中から選んだ数だけランダムで出題されます", (10, 25, 50, 100))

    data["course"] = course
    data["seikai"] = 0
    data["otetsuki"] = 0
    data["order"] = random.sample(list(range(1, 101)), course)

    st.button("開始", on_click=start, type="primary")


else:
    json2 = Path(__file__).parent.parent / "sample_data" / "yomifuda.json"
    with open(json2, "r", encoding="utf-8") as f:
        yomifuda = json.load(f)
    
    number = data["order"][st.session_state["j"]]
    uta = yomifuda[str(number)]

    st.text(f"{st.session_state["j"] + 1} / {data["course"]}")


    choices = data["choices"]
    if st.session_state["random"] == 0:
        dummy_numbers = random.sample(list(set(range(1, 101)) - set([number])), 3)

        choices = [[uta[1][1], 1]]
        for i in range(3):
            choices.append([yomifuda[str(dummy_numbers[i])][1][1], 0])
        random.shuffle(choices)

        data["choices"] = choices
        st.session_state["random"] = 1


    if st.session_state["choose"] == 0:
        with st.container(border=True):
            st.subheader(uta[0][0])
            st.text(uta[1][0])

        for i in range(4):
            if choices[i][1] == 1:
                st.button(choices[i][0], on_click=seikai, width="stretch")
            else:
                st.button(choices[i][0], on_click=otetsuki, width="stretch")


    else:
        with st.container(border=True):
            st.subheader(uta[0][0])
            st.text(f"{uta[1][0]}\n")

            st.subheader(uta[0][1])
            st.text(f"{uta[1][1]}\n")

            st.text(f"{number} {uta[2]}")


        if st.session_state["choose"] == 1:
            st.subheader("正解", divider="yellow")
            data["seikai"] += 1

        elif st.session_state["choose"] == 2:
            st.subheader("お手つき", divider="blue")
            data["otetsuki"] += 1


        with st.container(border=True):
            col1, col2 = st.columns(2)
            with col1:
                st.write("正解")
                st.subheader(data["seikai"])

            with col2:
                st.write("お手つき")
                st.subheader(data["otetsuki"])


        if st.session_state["j"] == data["course"] - 1:
            st.subheader("お疲れ様でした")
            st.button("もう一度最初から", on_click=reset, type="primary", width="stretch")

        else:
            st.button("次へ", on_click=next_uta, type="primary", width="stretch")


with open(json1, "w") as f:
    json.dump(data, f, indent=4)
