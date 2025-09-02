import streamlit as st
import pandas as pd

df = pd.read_csv("data.csv")

st.set_page_config(
    page_title = "Portfolio",
    layout="wide",

)

intro_left, intro_right = st.columns(2)

with intro_left:
    st.image("images/profile.jpg")
    st.write(f"Here's my Practice Portfolio using Streamlit")

with intro_right:
    st.title("RINZDEIL")
    st.info("""Here's my Portfolio using Streamlit. I am a newbie programmer learning python. 
    I am using my old Acer laptop to do this. The year is 2025. In the bleak midwinter. Flood control
    anomalies. Drinking Urbanica coffee with Majii    
    """)

st.text("Below you can find some of the apps I have built in Python. Feel free to contact me!")

body_left, body_right = st.columns(2)

with body_left:
    for index, row in df[0:2].iterrows():
        st.header(row["title"])
        st.text(row["description"])
        st.image(row["image"], width=300)

with body_right:
    for index, row in df[2:].iterrows():
        st.header(row["title"])