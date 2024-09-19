import streamlit as st
from streamlit import expander

st.title("Data Driven Rainfall Management:")
st.header("Building an Interactive Dashboard for "
          "Rainfall Trends and Statistics")


st.divider()
st.header("Presentation Flow:")
st.markdown("### Data Driven Management")
st.write("What is in the dashboard?")
st.write(" ")
st.markdown("### Python in Data Analysis")
st.write("How to code the dashboard?")
st.write(" ")
st.markdown("### Rainfall Dashboard Demo")
st.page_link("https://rainfalldashboardapp-hks9gxfbbsrskaslq846ip.streamlit.app/",
             label="Rainfall Analysis Dashboard")

st.divider()
st.markdown("### QR Codes:")
st.image("images/PRESENTATION.png")
st.image("images/RAINFALL DASHBOARD.png")
