import streamlit as st
import send_email as send

with st.form(key="email_form"):
  user_email = st.text_input("Enter your email")
  message_string = st.text_area("Enter your message")

  message = f"""\
Subject: PyPortfolio Leads

From: {user_email}

{message_string}
"""

  submit = st.form_submit_button("Submit")
  if submit:
    send.send_email(message)
    st.info("Your email was sent successfully")
