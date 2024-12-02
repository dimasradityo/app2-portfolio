import streamlit as st

st.title('Personal Projects')

with st.container(border=True):
    st.header('Resume')
    st.image('images/personal_projects/resume.png')
    st.write('Importing my static resume to a Python web app.')
    st.write(f"[Source Code](https://github.com/dimasradityo/resume-dimas-radityo)")