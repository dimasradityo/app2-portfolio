import streamlit as st

st.title('Personal Projects')

with st.container(border=True):
    st.header('[Resume](https://resumedimasradityo.streamlit.app/)')
    st.image('images/personal_projects/resume.png')
    st.write('Importing my static PDF resume to a Python web app.')
    st.write(f"[Source Code](https://github.com/dimasradityo/resume-dimas-radityo)")

with st.container(border=True):
    st.header('[News Aggregator](https://dimas-news-aggregator.streamlit.app/)')
    st.image('images/personal_projects/news_aggregator.png')
    st.write("Simple news aggregator to search for news based on user's search query. Data source is using API fron newsapi.org.")
    st.write(f"[Source Code](https://github.com/dimasradityo/news_aggregator)")