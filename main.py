import streamlit as st
import pandas as pd

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

content2 = """
"Below you can find some of the apps I have 
built in Python"
"""
st.write(content2)

col3, empty_col, col4 = st.columns([1.5,0.5,1.5])

df = pd.read_csv('data.csv', sep=';')

with col3:
    for index, row in df[:10].iterrows():
        st.header(row['title'])
        st.image(f"images/{row['image']}")
        st.write(row['description'])
        st.write(f"[Link to Repository]({row['url']})")

with col4:
    for index, row in df[10:].iterrows():
        st.header(row['title'])
        st.image(f"images/{row['image']}")
        st.write(row['description'])
        st.write(f"[Link to Repository]({row['url']})")