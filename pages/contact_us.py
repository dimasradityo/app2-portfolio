import streamlit as st
import send_email

st.header('Contact Me') 

with st.form(key='email_forms'):
    user_email = st.text_input('Your Email Address: ')
    user_message = st.text_area('Your message here...')
    full_message = f"""\
Subject: New Email From {user_email}

From: {user_email}
{user_message}
"""
    button = st.form_submit_button()
    if button:
        send_email.send_email(f"From {user_email}. {full_message}")
        st.info('Your email was sent successfully')