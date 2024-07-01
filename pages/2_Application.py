import streamlit as st
from streamlit_extras.switch_page_button import switch_page
from database_manager import *

connect_to_database()

st.set_page_config(layout="wide", initial_sidebar_state="collapsed")

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

st.markdown("""
    <style>
        .stApp{
            background-image: url('https://i.imgur.com/LmSlYc7.jpg');
            background-position: center center;
            background-repeat: no-repeat;
            background-size: 300% 300%;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown("<h1 style='line-height: 1.2; text-align: center; color: #05174B; margin-top: 100px;'>TESDAli: A Streamlined TESDA Assessment</br> Application Management System</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center; color: #05174B;'>Main Menu</h4>", unsafe_allow_html=True)

col1, col2, col3 = st.columns([1, 1, 1])

with col2:
    if st.button("Add a Record", use_container_width=True):
        switch_page("Insert")
    elif st.button("View Records", use_container_width=True):
        switch_page("View")
    elif st.button("Update a Record", use_container_width=True):
        switch_page("Update")
    elif st.button("Delete a Record", use_container_width=True):
        switch_page("Delete")

# Footer
st.markdown("""
<style>
        footer {
            background-color: #253C64;
            text-align: center;
            font-size: 12px;
            color: #FFFFFF;
            margin-top: 100px;
            padding-top: 20px;
            padding-bottom: 50px;
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
        padding-top: 0rem;  
        padding-left: 0rem; 
        padding-right: 0rem; 
        padding-bottom: 0rem; 
    }
    </style>
"""
st.markdown(hide_streamlit_bar, unsafe_allow_html=True)