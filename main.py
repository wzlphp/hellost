from langchain_core.messages import AIMessageChunk, HumanMessage
import streamlit as st
from langchain.agents import create_agent
from langchain_openai import ChatOpenAI
from langchain.tools import tool
import json
from loguru import logger
from langgraph.checkpoint.memory import InMemorySaver

 
 
# 定义模型
model = ChatOpenAI(
    model="deepseek/deepseek-v3.1-terminus",
    api_key="sk-fc27feb2aa6d3dac1131181fbde118073ed41863871113bf8b1ff24475483863",
    base_url="https://openai.qiniu.com/v1",
)

agent = create_agent(
    model=model,
    tools=[],
    system_prompt="你是一个专业的助手，你可以回答用户的问题。",
    checkpointer=InMemorySaver(),
)


# str = ''
# for data, matedata in agent.stream(
#     {"messages":HumanMessage(content="你好，我是张三。你是谁？")},
#     stream_mode="messages"
# ):
#     # print(matedata)
#     str += data.content_blocks[0]['text']
#     print(str)
#     print("\n")

# exit()

st.set_page_config(page_title="我是AI助手，有问题找我", page_icon="🤖", layout="centered")
st.markdown("<h5 style='text-align: center;'>🤖 我是AI助手，有问题找我</h5>", unsafe_allow_html=True)

# 初始化 session_state
if "messages" not in st.session_state:
    st.session_state.messages = []


# 显示历史消息
for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])


def token_get():
    for data, matedata in agent.stream(
        {"messages":HumanMessage(content=prompt)},
        stream_mode="messages",
        config={"configurable": {"thread_id": "123"}}
    ):
        if data.content_blocks:
            yield data.content_blocks[0]['text']

# 处理用户输入
if prompt := st.chat_input("请输入内容..."):
    # 1. 先显示用户消息
    st.chat_message("user").write(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    # 2. 调用你的大模型（这里先用模拟回复示范）
    # reply = f"AI：你刚才说的是：{prompt}"
    # result = agent.invoke({"messages":HumanMessage(content=prompt)})
    # reply = result["messages"][-1].content

    
    msg = st.chat_message("assistant")
    container = msg.empty()
    # reply = ""
    # for data, matedata in agent.stream({"messages":HumanMessage(content=prompt)}, stream_mode="messages"):
    #     if data.content_blocks:
    #         reply += data.content_blocks[0]['text']
    #         logger.info(reply)
    #         container.write_stream(reply)

    reply = container.write_stream(token_get())

    st.success("回答完成!")
    # 3. 显示 AI 消息并保存
    # st.chat_message("assistant").write(reply)
    st.session_state.messages.append({"role": "assistant", "content": reply})
