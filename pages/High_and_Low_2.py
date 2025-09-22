import json
from pathlib import Path

import streamlit as st

from model import high_and_low


st.title(":streamlit: High and Low Game!")
st.write("所持金を賭けて High か Low かを当てるゲーム")


json_path = Path(__file__).parent.parent / "sample_data" / "highlow_round3.json"
with open(json_path, "r", encoding="utf-8") as f:
    data = json.load(f)

if "i" not in st.session_state:
    st.session_state["i"] = 0
if "card" not in st.session_state:
    st.session_state["card"] = 0
if "judge" not in st.session_state:
    st.session_state["judge"] = 0
if "choice" not in st.session_state:
    st.session_state["choice"] = 0
if "delta_money" not in st.session_state:
    st.session_state["delta_money"] = 0
if "finish" not in st.session_state:
    st.session_state["finish"] = 0

def next_round():
    st.session_state["i"] += 1
    st.session_state["card"] = 0
    st.session_state["judge"] = 0


round_i = data["rounds"][st.session_state["i"]]
st.header(f"Round {round_i["round"]}")


if st.session_state["card"] == 0:
    if st.session_state["i"] == 0:
        round_i["chips_after"] = data["initial_chips"]
    else:
        round_i["chips_after"] = (data["rounds"]
                                      [st.session_state["i"] - 1]
                                      ["chips_after"])


st.subheader(f":moneybag: 所持金 {round_i["chips_after"]}")
bet = st.slider("いくら賭けますか？", 1, round_i["chips_after"])

if st.session_state["card"] == 0:
    round_i["bet"] = bet


if st.button("カードを引く"):
    if st.session_state["card"] == 0:
        st.session_state["card"] = 1

        if st.session_state["i"] == 0:
            card_draw = high_and_low.card(data["deck"])

        else:
            card_draw = high_and_low.card(data["rounds"]
                                            [st.session_state["i"] - 1]
                                            ["remaining_deck"])

        round_i["base_card"] = card_draw[0]
        round_i["result_card"] = card_draw[1]
        round_i["remaining_deck"] = card_draw[2]


if st.session_state["card"] != 0:
    with st.container(border=True):
        col1, col2 = st.columns(2)
        with col1:
            st.write("現在のカード")
            st.subheader(round_i["base_card"])
        with col2:
            st.write(":moneybag: Bet")
            st.subheader(round_i["bet"])


    choice = st.radio(f"{round_i["base_card"]} より 大きい(High)？ 小さい(Low)？",
                      ["High", "Low"])
        
    if st.button("結果を見る"):
        if st.session_state["judge"] == 0:
            st.session_state["choice"] = choice
            st.session_state["judge"] = high_and_low.judge(choice,
                                                           round_i["base_card"],
                                                           round_i["result_card"])
            
            after_money = high_and_low.bet(st.session_state["judge"],
                                   round_i["chips_after"],
                                   round_i["bet"])
            st.session_state["delta_money"] = after_money - round_i["chips_after"]
            round_i["chips_after"] = after_money


if st.session_state["judge"] != 0:
    with st.container(border=True):
        col1, col2 = st.columns(2)
        with col1:
            st.write("Result")
            st.subheader(round_i["result_card"])
        with col2:
            st.write("Your choice")
            st.subheader(st.session_state["choice"])

    round_i["outcome"] = st.session_state["judge"]
    

    if st.session_state["judge"] == "Win":
        st.success("You Win!")
    elif st.session_state["judge"] == "Lose":
        st.error("You Lose...")
    else:
        st.info("Draw")

    st.metric(":moneybag: 所持金", round_i["chips_after"], st.session_state["delta_money"])


    if round_i["chips_after"] <= 0:
            st.session_state["finish"] = 1
            data["game_end"] = "failure"
            st.header("Failure!")
            st.snow()

    elif round_i["round"] == 3:
        st.session_state["finish"] = 1
        data["game_end"] = "3 rounds finished"
        st.header("3 rounds finished!")
        st.balloons()

    else:
        st.button("Next Round", on_click=next_round, type="primary")


if st.session_state["finish"] != 0:
    with st.container(border=True):
        col1, col2, col3 = st.columns(3)
        with col1:
            outcome = data["rounds"][0]["outcome"]
            st.write("Round 1")
            st.subheader(outcome)
            if outcome == "Win":
                st.subheader(":tada:")
            elif outcome == "Lose":
                st.subheader(":money_with_wings:")

        with col2:
            if round_i["round"] > 2:
                outcome = data["rounds"][1]["outcome"]
                st.write("Round 2")
                st.subheader(outcome)
                if outcome == "Win":
                    st.subheader(":tada:")
                elif outcome == "Lose":
                    st.subheader(":money_with_wings:")

        with col3:
            if round_i["round"] == 3:
                outcome = data["rounds"][2]["outcome"]
                st.write("Round 3")
                st.subheader(outcome)
                if outcome == "Win":
                    st.subheader(":tada:")
                elif outcome == "Lose":
                    st.subheader(":money_with_wings:")


with open(json_path, "w") as f:
    json.dump(data, f, indent=4)
