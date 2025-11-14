import streamlit as st

st.set_page_config(page_title="多轮对话 Demo", page_icon="🤖")
st.title("🤖 多轮对话聊天 Demo")

# 初始化 session_state
if "messages" not in st.session_state:
    st.session_state.messages = []


# 显示历史消息
for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])


# 处理用户输入
if prompt := st.chat_input("请输入内容..."):
    # 1. 先显示用户消息
    st.chat_message("user").write(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    # 2. 调用你的大模型（这里先用模拟回复示范）
    reply = f"AI：你刚才说的是：{prompt}"

    # 3. 显示 AI 消息并保存
    st.chat_message("assistant").write(reply)
    st.session_state.messages.append({"role": "assistant", "content": reply})
