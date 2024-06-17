import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from database_manager import *
import plotly.graph_objects as go
from streamlit_extras.switch_page_button import switch_page

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
        align-items: center;
        justify-content: space-between;
        background: rgba(0, 0, 0, 0.05);
        padding: 10px;
        border-radius: 10px;
        color: #05174B;
    }
    .logo-text-container {
        display: flex;
        align-items: center;
        margin-left: 50px;
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
        display: flex;
        margin-bottom: 20px;
        margin-right: 60px;
    }
    .navigation a {
        margin-top: 30px;
        text-decoration: none;
        color: #05174B;
        font-size: 12px;
        border-radius: 15px;
        padding: 8px 15px;
        margin-left: 15px;
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

# Fetch data from the database
learners_data, learners_columns = fetch_learners()
application_data, application_columns = fetch_applications()
work_exp_data, work_exp_columns = fetch_work_experiences()

# Convert data to pandas DataFrames
learners_df = pd.DataFrame(learners_data, columns=learners_columns)
application_df = pd.DataFrame(application_data, columns=application_columns)
work_exp_df = pd.DataFrame(work_exp_data, columns=work_exp_columns)

# Metrics
col1, col2, col3, col4, col5 = st.columns([3, 1, 1, 1, 1])
col1.markdown("<h1 style='color: blue; text-align: center;'>TESDA Dashboard</h1>", unsafe_allow_html=True)
col2.metric("Courses Offered", len(application_df['Assessment_Title'].unique()), "Assessments")
col3.metric("Total Learners", len(learners_df), "Learners")
col4.metric("Total Applications", len(application_df), "Applications")
# Check if there are any NaN values in the 'Age' column
if len(learners_df) == 0:
    col5.metric("Average Age of Learners", "--", "Age")
else:
    col5.metric("Average Age of Learners", round(learners_df['Age'].mean()), "Age")

st.write(" ")
st.write(" ")
st.write(" ")
st.write(" ")

tab1, tab2 = st.tabs(["Summary", "Dataframes"])
with tab1:
    col1, col2, col3 = st.columns(3)
    with col1:
        st.subheader("Assessment Titles Distribution")
        assessment_title_counts = application_df['Assessment_Title'].value_counts().reset_index()
        assessment_title_counts.columns = ['Assessment Title', 'Count']
        st.dataframe(assessment_title_counts, hide_index=True, use_container_width=True)

    with col2:
        st.subheader("Top Training Centers")
        top_training_centers = application_df['Training_Center'].value_counts().reset_index()
        top_training_centers.columns = ['Training Center', 'Count']
        st.dataframe(top_training_centers, hide_index=True, use_container_width=True)

    with col3:
        #Dictionary to map assessment status
        assessment_status_mapping = {
            "FQ": "Full Qualification",
            "COC": "Certificate of Competency",
            "R": "Renewal"
        }
        st.subheader("Assessment Status Distribution")
        application_df['Assessment_Status'] = application_df['Assessment_Status'].map(assessment_status_mapping)
        assessment_status_counts = application_df['Assessment_Status'].value_counts().reset_index()
        assessment_status_counts.columns = ['Assessment Status', 'Count']
        st.dataframe(assessment_status_counts, hide_index=True, use_container_width=True)
        
    st.write(" ")
    st.write(" ")
    st.write(" ")
    st.write(" ")
    col4, col5, col6, col7 = st.columns(4)

    with col4:
        client_type_mapping_long = {
            "TVETGS": "TVET Graduating Student",
            "TVETG": "TVET graduate",
            "IW": "Industry worker",
            "K-12": "K-12",
            "OWF": "Overseas Filipino Worker"
        }

        learners_df['Client_Type'] = learners_df['Client_Type'].map(client_type_mapping_long)
        st.subheader("Client Types")
        client_type_counts = learners_df['Client_Type'].value_counts()
        fig = go.Figure(data=[go.Pie(labels=client_type_counts.index, values=client_type_counts, hole=0.2)])
        fig.update_layout(
            width=500,
            height=500
        )
        st.plotly_chart(fig)

    with col5:
        st.subheader("Applications Over Time")
        application_df['Application_Date'] = pd.to_datetime(application_df['Application_Date'])
        applications_over_time = application_df.groupby(application_df['Application_Date'].dt.to_period('M')).size()
        applications_over_time.index = applications_over_time.index.to_timestamp()
        st.line_chart(applications_over_time)

    with col6:
        st.subheader("Age Distribution")
        fig2, ax2 = plt.subplots()
        sns.histplot(learners_df['Age'], bins=10, ax=ax2)
        st.pyplot(fig2)

    with col7:
        st.subheader("Sex Distribution")
        sex_counts = learners_df['Sex'].value_counts()
        fig, ax = plt.subplots()
        ax.pie(sex_counts, labels=sex_counts.index, autopct='%1.1f%%', startangle=90)
        ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle
        st.pyplot(fig)

with tab2:  
    # DataFrames
    st.subheader("Learners")
    st.dataframe(learners_df, height=300, hide_index=True)

    col1, col2 = st.columns([1, 1])
    with col1:
        st.subheader("Applications")
        st.dataframe(application_df, height=300, hide_index=True, use_container_width=True)
    with col2: 
        st.subheader("Work Experiences")
        st.dataframe(work_exp_df, height=300, hide_index=True, use_container_width=True)

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
    st.button("Add a Record", disabled=True, use_container_width=True)
with col3:
    if st.button("View Records", use_container_width=True):
        switch_page("View")
with col4:
    if st.button("Update a Record", use_container_width=True):
        switch_page("Update")
with col5:
    if st.button("Delete a Record", use_container_width=True):
        switch_page("Delete")

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
        margin-top: 80px;
    }
</style>
<footer>
        This website is an independent project and is not affiliated with TESDA. It is intended solely for academic purposes.
</footer>
""", unsafe_allow_html=True)