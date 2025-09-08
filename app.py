import streamlit as st


tabs = ["Home", "掛け算", "3"]
tab1, tab2, tab3 = st.tabs(tabs)


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
    st.title("3")
