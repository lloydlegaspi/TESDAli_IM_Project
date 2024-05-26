import streamlit as st
from streamlit_extras.switch_page_button import switch_page
from database_manager import *

connect_to_database()

st.set_page_config(layout="wide", initial_sidebar_state="collapsed")

# Custom CSS for the button
m = st.markdown("""
    <style>
    div.stButton > button:first-child {
        box-shadow:inset 0px 1px 0px 0px #bbdaf7;
        background:linear-gradient(to bottom, #79bbff 5%, #378de5 100%);
        background-color:#79bbff;
        border-radius:6px;
        border:1px solid #84bbf3;
        display:inline-block;
        cursor:pointer;
        color:#ffffff;
        font-family:Arial;
        font-size:15px;
        font-weight:bold;
        padding:6px 24px;
        text-decoration:none;
        text-shadow:0px 1px 0px #528ecc;
    }
    div.stButton > button:hover {
        background: linear-gradient(#378de5, #79bbff);
    }
    div.stButton > button:active {
        position:relative;
        top:3px;
    }
    
    </style>""", unsafe_allow_html=True)

col1, col2, col3 = st.columns([3, 1, 6])

with col2:
    st.image("images/logo.png", width=150)

with col3:
    st.markdown("<h4 style='line-height: 0.3;'>Republic of the Philippines</h4>", unsafe_allow_html=True)
    st.markdown("<h4 style='line-height: 0.6;'>TECHNICAL EDUCATION AND SKILLS DEVELOPMENT AUTHORITY</h1>", unsafe_allow_html=True)
    st.markdown("<h4 style='line-height: 0.5;'>Pangasiwaan sa Edukasyong Teknikal at Pagpapaunlad ng Kasanayan</h4>", unsafe_allow_html=True)

st.write(" ")
st.write(" ")
st.write(" ")
st.write(" ")
st.write(" ")
st.write(" ")
st.write(" ")
st.write(" ")
st.write(" ")
st.write(" ")
st.write(" ")
st.write(" ")
st.markdown("<h1 style='line-height: 0.6; text-align: center; color: blue;'>TESDAli: A Streamlined TESDA Assessment Application Management System</h1>", unsafe_allow_html=True)

col1, col2, col3 = st.columns([1, 1, 1])

with col2:
    st.write(" ")
    st.write(" ")
    st.write(" ")
    if st.button("Add a Record", use_container_width=True):
        switch_page("Insert")
    elif st.button("View Records", use_container_width=True):
        switch_page("View")
    elif st.button("Update a Record", use_container_width=True):
        switch_page("Update")
    elif st.button("Delete a Record", use_container_width=True):
        switch_page("Delete")