import json
from pathlib import Path
import streamlit as st

st.title("High and Low Game!")
st.write("High か Low かを当ててください。")

# ----Pathを指定して JSONファイルを読み込み ----
json_path = Path(__file__).parent.parent / "sample_data" / "highlow_round3.json"
with open(json_path, "r", encoding="utf-8") as f:
    data = json.load(f)

if "i" not in st.session_state:
    st.session_state["i"] = 0

st.session_state["deck"] = data["deck"]
st.session_state["rounds"] = data["rounds"]

round_i = st.session_state["rounds"][st.session_state["i"]]

st.write(f"Round {round_i["round"]}")
st.write(f"現在のカード: {round_i["base_card"]}")

flag = 0
if st.button("High"):
    if round_i["base_card"] < round_i["result_card"]:
        round_i["outcome"] = "win"
    else:
        round_i["outcome"] = "lose"
    flag = 1

if st.button("Low"):
    if round_i["base_card"] > round_i["result_card"]:
        round_i["outcome"] = "win"
    else:
        round_i["outcome"] = "lose"
    flag = 1

if flag == 1:
    st.write(f"Result: {round_i["result_card"]}")
    if round_i["outcome"] == "win":
        st.success("You Win!")
    else:
        st.error("You Lose")
    st.session_state["i"] += 1

    if round_i["round"] < 3:
        st.button("Next Round")

with open(json_path, "w") as f:
    json.dump(data, f, indent=4)
