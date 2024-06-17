import streamlit as st

def load_about():
    with open("About.html", "r", encoding="utf-8") as file:
        about_html = file.read()
    return about_html

def main():
    st.set_page_config(layout="wide", initial_sidebar_state="collapsed")
    about_html = load_about()
    st.write(about_html, unsafe_allow_html=True)  

if __name__ == "__main__":
    main()
