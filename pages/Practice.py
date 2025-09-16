import streamlit as st


tabs = ["Home", "掛け算", "カウント", "ラウンド"]
tab1, tab2, tab3, tab4 = st.tabs(tabs)


with tab1:
    st.title("Hello, Streamlit!")


with tab2:
    st.title("掛け算")

    input1 = st.number_input("1つ目の数字を入力してください", value=0)
    input2 = st.number_input("2つ目の数字を入力してください", value=0)

    result = input1 * input2

    st.subheader("計算結果")
    st.write(f"{input1} × {input2} = {result}")


with tab3:
    st.title("カウント")

    # 初期化
    if "count" not in st.session_state:
        st.session_state.count = 0

    # 更新
    if st.button("カウントアップ"):
        st.session_state.count += 1

    # 表示
    st.write("カウント:", st.session_state.count)


with tab4:
    st.title("ラウンド")

    qp = st.query_params
    round_num = int(qp.get("round", "1"))  # なければ 1
    st.write(f"現在のラウンド: {round_num}")

    if st.button("次のラウンドへ"):
        round_num += 1
        st.query_params["round"] = str(round_num)  # URLを更新
        st.write(f"次のラウンドは {round_num} です")
