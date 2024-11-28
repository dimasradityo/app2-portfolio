import streamlit as st

st. set_page_config(layout='wide')

col1, col2 = st.columns(2)

with col1:
    st.image("images/1.png")

with col2:
    st.title("Dimas Radityo")
    content = """
    Placeholder content for now
"""
    st.info(content)