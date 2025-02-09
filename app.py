#解答例

import streamlit as st
import random
st.title("ランダム数字ジェネレーター")
# 数字の個数を選択
num_count = st.slider("表示する数字の個数", 1, 10, 5) #スライダーで数字の個数を選択

if st.button("ランダムな数字を生成"):
    for i in range(num_count):
        random_number = random.randint(1, 100)
    st.write(f"生成された数字: {random_number}")