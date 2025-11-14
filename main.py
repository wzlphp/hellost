import streamlit as st

menus = st.sidebar.title(":blue[Chat]:red[Bot]")


def handle_prompt(prompt):
    st.write(f"您输入的问题是：{prompt}")


prompt = st.chat_input("请输入您的问题", key="prompt", max_chars=50, accept_file=False, on_submit="handle_prompt")
