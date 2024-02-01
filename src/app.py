import streamlit as st
from predict_page import show_predict_page
from explore_page import show_explore_page


#Create sidebar
page = st.sidebar.selectbox("Explore Or Predict", ("Predict", "Explore"))

if page == "Predict":
    #Show the prediction page
    show_predict_page()
else:
    show_explore_page()