import streamlit as st

def load_about():
    with open("About.html", "r", encoding="utf-8") as file:
        about_html = file.read()
    return about_html

def main():
    st.set_page_config(layout="wide", initial_sidebar_state="collapsed")
    about_html = load_about()
    st.balloons()
    st.write(about_html, unsafe_allow_html=True)  

if __name__ == "__main__":
    main()

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
