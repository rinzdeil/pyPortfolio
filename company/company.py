import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Company Portfolio",
    layout="wide"
)

st.header("The Best Company")
st.text("""
Welcome to Company Name, where innovation meets excellence. We are dedicated to delivering top-tier solutions tailored to your needs. Our team of experts is committed to driving success through cutting-edge technology and unparalleled service.
Discover our wide range of services designed to help your business thrive. From strategic consulting to advanced technical support, we ensure your goals become a reality.
At Company Name we believe in building lasting partnerships. With years of industry experience and a passion for innovation, we strive to exceed expectations and empower your growth.
Reach out to us to learn more about how we can collaborate. We value every inquiry and look forward to connecting with you.
""")

st.subheader("Our Team")


spacing = 0.5
body_left, space_left, body_mid, space_right, body_right = st.columns([1, spacing, 1, spacing, 1])

def iterate_csv(start):
    df = pd.read_csv(f"company/data.csv", header=0)
    end = start + 4
    for index, row in df[start:end].iterrows():
        name = f"{row['first name']} {row['last name']}".title()
        st.subheader(name)
        st.info(row["role"])
        st.image("company/images/" + row["image"])

with body_left:
    iterate_csv(0)

with body_mid:
    iterate_csv(4)

with body_right:
    iterate_csv(8)

