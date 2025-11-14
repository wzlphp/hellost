import streamlit as st
# Add a selectbox to the sidebar:
add_selectbox = st.sidebar.selectbox(
    'How would :blue[you] :red[like] to be contacted?:sunglasses:',
    ('Email', 'Home phone', 'Mobile phone')
)

# Add a slider to the sidebar:
add_slider = st.sidebar.slider(
    'Select a range of values',
    0.0, 100.0, (25.0, 75.0)
)

st.badge('这是一个错误信息')
st.code('''
import streamlit as st
import pandas as pd
from datetime import time, datetime
''')


st.header("_Streamlit_ is :blue[cool] :sunglasses:")
st.header("This is a header with a divider", divider="gray")
st.header("These headers have rotating dividers", divider=True, anchor=False)
st.header("One", divider=True)
st.header("Two", divider=False)
st.header("Three", divider=True)
st.header("Four", divider=True)


