import streamlit as st
from streamlit_extras.switch_page_button import switch_page

st.set_page_config(layout="wide", initial_sidebar_state="collapsed")
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
    if st.button("Apply Now!", use_container_width=True):
        switch_page("Application Form")