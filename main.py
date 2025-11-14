import streamlit as st
# Add a selectbox to the sidebar:
add_selectbox = st.sidebar.selectbox(
    'How would you like to be contacted?:sunglasses:',
    ('Email', 'Home phone', 'Mobile phone')
)

# Add a slider to the sidebar:
add_slider = st.sidebar.slider(
    'Select a range of values',
    0.0, 100.0, (25.0, 75.0)
)

st.badger('这是一个错误信息')
st.code('''
import streamlit as st
import pandas as pd
from datetime import time, datetime
''')
