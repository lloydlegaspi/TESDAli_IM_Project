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

# Custom CSS for the button and header
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
    
        header {
        display: flex;
        background: rgba(255, 255, 255, 0.9); 
        color: #05174B;
        width: 100%; 
        padding: 10px 0;
        position: fixed; 
        top: 0; 
        left: 0; 
        right: 0; 
        z-index: 1000; 
        transition: top 0.3s; 
        box-shadow: 0px 2px 5px rgba(0, 0, 0, 0.1); 
    }

        .logo-text-container {
            display: flex;
            align-items: center;
            margin-right: auto;
            margin-left: 75px;
        }
        .logo img {
            width: 40px;
            margin-right: 20px;
        }
        .text-container {
            font-family: Arial, sans-serif;
            font-size: 12px;
        }
        .text-container p {
            font-size: 12px;
            margin: 0;
            padding: 0;
        }
        .navigation {
            align-items: right;
            display: flex;
            margin-bottom: 20px;
            margin-left: auto;
            margin-right: 75px;
            gap: 20px;
        }
        .navigation a {
            margin-top: 25px;
            text-decoration: none;
            color: #05174B;
            font-size: 13px; 
            border-radius: 15px;
            padding: 8px 10px; 
        }
        .navigation a.selected {
            background-color: #5C6B8B; 
            color: #FFFFFF; 
        }
        .navigation a:hover {
            background-color: #1A4793; 
            color: #FFFFFF; 
        }
    </style>
""", unsafe_allow_html=True)

# Header
st.markdown("""
    <header>
        <div class="logo-text-container">
            <div class="logo">
                <img src="https://edgedavao.net/wp-content/uploads/2018/07/37768545_1284993581638137_4466808018389958656_n-2.png" alt="Logo">
            </div>
            <div class="text-container">
                <p>Republic of the Philippines</p>
                <p><b>TECHNICAL EDUCATION AND SKILLS DEVELOPMENT AUTHORITY</b></p>
                <p>Pangasiwaan sa Edukasyong Teknikal at Pagpapaunlad ng Kasanayan</p>
            </div>
        </div>
        <div class="navigation">
            <a href="/Home" target="_self">Home</a>
            <a href="/Application" target="_self" class="selected">Application</a>
            <a href="/About" target="_self">About</a>
        </div>
    </header>
""", unsafe_allow_html=True)

st.write(" ")
st.write(" ")

st.markdown("<h1 style='color: blue; text-align:center;'>Delete a Record</h1>", unsafe_allow_html=True)

# Initialize session state for selected record
if 'record' not in st.session_state:
    st.session_state.record = None
if 'columns' not in st.session_state:
    st.session_state.columns = None
    
col1, col2, col3 = st.columns([1, 5, 1])
with col2:
    # Select table
    table = st.selectbox("Select Table", ["Learners", "Application", "Work_Exp"])

    # Enter record ID
    record_id = st.number_input("Enter Record ID", min_value=1, step=1)

    # Fetch and display the record
    if st.button("Fetch Record"):
        record, columns = fetch_record(table, record_id)
        if record is not None and columns is not None:
            st.session_state.record = record
            st.session_state.columns = columns
        else:
            st.warning(f"No record found with ID {record_id} in {table} table")

    st.write(" ")
    st.write(" ")

    # Display the fetched record
    if st.session_state.record is not None and st.session_state.columns is not None:
        record_df = pd.DataFrame([st.session_state.record], columns=st.session_state.columns)
        st.write(record_df)

        # Confirm and delete the record
        if st.button("Delete Record"):
            success, message = delete_record(table, record_id)
            if success:
                st.success(message)
                # Reset session state
                st.session_state.record = None
                st.session_state.columns = None
            else:
                st.error(message)

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


# Footer
st.markdown("""
<style>
    footer {
        background-color: #253C64;
        text-align: center;
        margin: 20px 0;
        font-size: 12px;
        color: #FFFFFF;
        padding: 30px;
        border-radius: 10px;
        margin-top: 30px;
    }
</style>
<footer>
        This website is an independent project and is not affiliated with TESDA. It is intended solely for academic purposes.
</footer>
""", unsafe_allow_html=True)

hide_streamlit_bar = """
    <style>
    /* Hide the Streamlit top bar using its specific class */
    .st-emotion-cache-uc1cuc {
        display: none !important;
    }
    /* Optional: Adjust the main content area if necessary */
    .main .block-container {
        padding-top: 3rem;  
        padding-left: 5rem; 
        padding-right: 5rem; 
        padding-bottom: 0rem; 
    }
    </style>
"""
st.markdown(hide_streamlit_bar, unsafe_allow_html=True)