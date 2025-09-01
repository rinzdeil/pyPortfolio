import streamlit as st

st.set_page_config(
    page_title = "Portfolio",
    layout="wide"
)

left, right = st.columns(2)

with left:
    st.title("RINZDEIL")
    st.write(f"Here's my Practice Portfolio using Streamlit")

with right:
    st.text("Here's my Portfolio using Streamlit")