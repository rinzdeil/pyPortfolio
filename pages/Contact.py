import streamlit as st

with st.form(key="email_form"):
  user_email = st.text_input("Enter your email")
  message = st.text_area("Enter your message")
  submit = st.form_submit_button("Submit")
  if submit:
    print(f"{user_email} Submitted!")


  
