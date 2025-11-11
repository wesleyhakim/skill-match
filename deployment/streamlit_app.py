import streamlit as st
import home
import prediction

st.set_page_config(
    page_title="SkillMatch | Smart Job Recommendation",
    page_icon="./src/image.png",
    layout="wide",
    initial_sidebar_state='expanded'
)

page = st.sidebar.selectbox("Pilih Page : ", ("👋Home Page", "🖊️Aplikasi"))

if page == "👋Home Page":
    home.run()
else:
    prediction.run()