import streamlit as st
import pandas as pd

st.title("RAG 问答系统")


st.header("st.*button*:sunglasses:")

if st.button("点击我"):
    st.write("按钮被点击了！")
else:
    st.write("按钮未被点击")

df = pd.DataFrame({
     'first column': [1, 2, 3, 4, 5],
     'second column': [10, 20, 30, 40, 50]
     })
st.write(df)


age = st.slider('How old are you?', 0, 130, 25)
st.write("I'm ", age, 'years old')