import streamlit as st

def load_homepage():
    with open("Home.html", "r") as file:
        homepage_html = file.read()
    return homepage_html

def main():
    st.set_page_config(layout="wide", initial_sidebar_state="collapsed")
    st.markdown(load_homepage(), unsafe_allow_html=True)

if __name__ == "__main__":
    main()
