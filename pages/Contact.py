import streamlit as st
import send_email as send
import pandas as pd

TOPICS_PATH = "./company/topics.csv"
df = pd.read_csv(TOPICS_PATH)

with st.form(key="email_form"):
  user_email = st.text_input("Enter your email", key="email")
  topic = st.selectbox("What topic do you want to discuss?", df["topic"])
  message_string = st.text_area("Enter your message")
  submit = st.form_submit_button("Submit")

  message = f"""\
Subject: PyPortfolio Leads

From: {user_email}
Topic: {topic}

{message_string}
"""

  if submit:
    send.send_email(message)
    st.info("Your email was sent successfully")
