import streamlit as st
from database_manager import *
from streamlit_extras.switch_page_button import switch_page
import pandas as pd

st.set_page_config(layout="wide", initial_sidebar_state="collapsed")
logo_path = "images/logo.png"

# Custom CSS for the button
m = st.markdown("""
    <style>
    div.stButton > button:first-child {
        box-shadow:inset 0px 1px 0px 0px #97c4fe;
        background:linear-gradient(to bottom, #3d94f6 5%, #1e62d0 100%);
        background-color:#3d94f6;
        border-radius:6px;
        border:1px solid #337fed;
        display:inline-block;
        cursor:pointer;
        color:#ffffff;
        font-family:Arial;
        font-size:15px;
        font-weight:bold;
        padding:6px 24px;
        text-decoration:none;
        text-shadow:0px 1px 0px #1570cd;
    }
    div.stButton > button:hover {
        background: linear-gradient(#378de5, #79bbff);
    }
    div.stButton > button:active {
        position:relative;
        top:3px;
    }
    
    </style>""", unsafe_allow_html=True)

col1, col2, col3 = st.columns([1, 1, 7])

with col2:
    st.image(logo_path, width=150)

with col3:
    st.markdown("<h4 style='line-height: 0.3;'>Republic of the Philippines</h4>", unsafe_allow_html=True)
    st.markdown("<h1 style='line-height: 0.6;'>TECHNICAL EDUCATION AND SKILLS DEVELOPMENT AUTHORITY</h1>", unsafe_allow_html=True)
    st.markdown("<h4 style='line-height: 0.5;'>Pangasiwaan sa Edukasyong Teknikal at Pagpapaunlad ng Kasanayan</h4>", unsafe_allow_html=True)

st.write(" ")
st.write(" ")

st.markdown("<h1 style='color: blue; text-align:center;'>Delete a Record</h1>", unsafe_allow_html=True)

col1, col2, col3 = st.columns([1, 5, 1])
with col2:
    # Select table
    table = st.selectbox("Select Table", ["Learners", "Application", "Work_Exp"])

    # Enter record ID
    record_id = st.number_input("Enter Record ID", min_value=1, step=1)

    # Fetch and display the record
    if st.button("Fetch Record"):
        record, columns = fetch_record(table, record_id)
        if record is None and columns is None:
            st.warning(f"No record found with ID {record_id} in {table} table")
        record_df = pd.DataFrame(record, columns)
        st.write(record_df)

        st.write(" ")
        st.write(" ")

        # Confirm deletion
        if st.button("Delete Record"):
            if record_id:
                success, message = delete_record(table, record_id)
                if success:
                    st.success(message)
                else:
                    st.error(message)
            else:
                st.warning("Please enter a valid record ID")

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
st.write(" ")

# Navigation buttons
col1, col2, col3, col4, col5 = st.columns([1, 1, 1, 1, 1,])
with col1:
    if st.button("Back to Home", use_container_width=True):
        switch_page("Home")
with col2:
    if st.button("Add a Record", use_container_width=True):
        switch_page("Insert")
with col3:
    if st.button("View Records", use_container_width=True):
        switch_page("View")
with col4:
    if st.button("Update a Record", use_container_width=True):
        switch_page("Update")
with col5:
    st.button("Delete a Record", disabled=True, use_container_width=True)
st.write(" ")