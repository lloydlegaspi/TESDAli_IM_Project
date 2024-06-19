import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from database_manager import *
import plotly.graph_objects as go
from streamlit_extras.switch_page_button import switch_page
import plotly.express as px

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
courses_offered, total_learners, total_applications, average_age = fetch_metrics()

# Example usage of displaying metrics (assuming you use streamlit)
col1, col2, col3, col4, col5 = st.columns([3, 1, 1, 1, 1])
col1.markdown("<h1 style='color: blue; text-align: center;'>TESDA Dashboard</h1>", unsafe_allow_html=True)
col2.metric("Courses Offered", courses_offered, "Assessments")
col3.metric("Current Learners", total_learners, "Learners")
col4.metric("Total Applications", total_applications, "Applications")
col5.metric("Learners' Average Age", average_age, "Age")

st.write(" ")
st.write(" ")

tab1, tab2, tab3 = st.tabs(["Application Summary", "Learners' Profile", "Others"])

with tab1:
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Assessment Titles Distribution")
        assessment_df = fetch_assessment_titles_distribution()
        if assessment_df:
                df = pd.DataFrame(assessment_df, columns=['Assessment Title', 'Count'])
                df = df.sort_values(by='Count')

                plt.figure(figsize=(10, 6))
                bars = plt.barh(df['Assessment Title'], df['Count'], color='skyblue')
                plt.xlabel('Applications')
                plt.xticks(range(0, max(df['Count']) + 1, 1))
                plt.yticks([])
                plt.tight_layout()
                
                for i, bar in enumerate(bars):
                    plt.text(bar.get_width(), bar.get_y() + bar.get_height()/2, 
                            df['Assessment Title'].iloc[i], 
                            ha='center', va='center', 
                            fontsize=12, color='black')
                st.pyplot(plt)

    with col2:
        st.subheader("Top Training Centers")
        training_centers_df = fetch_top_training_centers()
        if training_centers_df:
                df = pd.DataFrame(training_centers_df, columns=['Training Center', 'Count'])
                df = df.sort_values(by='Count')

                plt.figure(figsize=(10, 6))
                bars = plt.barh(df['Training Center'], df['Count'], color='skyblue')
                plt.xlabel('Applications')
                plt.xticks(range(0, max(df['Count']) + 1, 1))
                plt.yticks([])
                plt.tight_layout()
                
                for i, bar in enumerate(bars):
                    plt.text(bar.get_width(), bar.get_y() + bar.get_height()/2, 
                            df['Training Center'].iloc[i], 
                            ha='center', va='center', 
                            fontsize=12, color='black')
                    
                st.pyplot(plt)
    
    col4, col5 = st.columns(2)
    with col1:
        st.subheader("Assessment Status Distribution")
        data = fetch_assessment_status_distribution()

        if data:
            df = pd.DataFrame(data, columns=['Assessment Status', 'Count'])

            plt.figure(figsize=(10, 6))
            bars = plt.bar(df['Assessment Status'], df['Count'], color='skyblue')
            plt.ylabel('Applications')
            plt.yticks(range(0, max(df['Count']) + 1, 1))
            plt.tight_layout()
            st.pyplot(plt)
        
    with col2:
        st.subheader("Applications Over Time")
        data = fetch_applications_over_time()

        if data:
            df = pd.DataFrame(data, columns=['Month', 'Count'])
            df['Month'] = pd.to_datetime(df['Month'])
            df.set_index('Month', inplace=True)

            # Plotting with Matplotlib
            plt.figure(figsize=(10, 6))
            months = [row[0] for row in data] 
            counts = [row[1] for row in data]
            plt.plot(months, counts, marker='o', linestyle='-')
            plt.xlabel('Month')
            plt.ylabel('No. of Applications')
            plt.xticks(range(1, 13), ['Jan', 'Feb', 'March', 'April', 'May', 'June',
                                    'July', 'Aug', 'Sept', 'Oct', 'Nov', 'Dec'])
            plt.yticks(range(0, max(df['Count']) + 1, 1))
            plt.tight_layout()

            # Display the plot using Streamlit
            st.pyplot()
            
        st.write(" ")
        st.write(" ")

with tab2:
    col1, col2, col3 = st.columns(3)

    with col1:
        st.subheader("Client Type")
        data = fetch_client_type_distribution()

        if data:
            df = pd.DataFrame(data, columns=['Client Type', 'Count'])
            blues = ['#0000ff', '##31b1e0', '#7ed1e6', '#0000b2', '#000099']

            # Plotting Client Type Distribution with Plotly
            fig = go.Figure(data=[go.Pie(labels=df['Client Type'], values=df['Count'], hole=0.2, 
                                         marker=dict(colors=blues))])
            fig.update_traces(textposition='inside', textinfo='label+percent', showlegend=False)
            fig.update_layout(
                width=500,
                height=500
            )
            st.plotly_chart(fig)

    with col2:
        st.subheader("Age Distribution")
        age_data = fetch_age_distribution()

        if age_data:
            age_df = pd.DataFrame(age_data, columns=['Age', 'Count'])
            fig2, ax2 = plt.subplots()
            sns.barplot(x='Age', y='Count', data=age_df, ax=ax2)
            ax2.set_xlabel("Age")
            ax2.set_ylabel("Applications")
            plt.yticks(range(0, max(df['Count']) + 1, 1))
            st.pyplot(fig2)

    with col3:
        st.subheader("Sex Distribution")
        sex_data = fetch_sex_distribution()

        if sex_data:
            sex_df = pd.DataFrame(sex_data, columns=['Sex', 'Count'])
            fig, ax = plt.subplots()
            ax.pie(sex_df['Count'], labels=sex_df['Sex'], autopct='%1.1f%%', startangle=90, colors=["#1f77b4", "#7ed1e6"])
            ax.axis('equal') 
            st.pyplot(fig)  
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.subheader("Average Salary by Employment Status")
        salary_data = fetch_avg_salary_by_emp_status()

        if salary_data:
            salary_df = pd.DataFrame(salary_data, columns=['Employment Status', 'Average Salary'])
            fig, ax = plt.subplots()
            bars = ax.barh(salary_df['Employment Status'], salary_df['Average Salary'], color='skyblue')
            ax.set_xlabel('Average Salary')

            # Add labels to the bars
            for bar in bars:
                width = bar.get_width()
                ax.text(width, bar.get_y() + bar.get_height() / 2,
                        f'{width:.2f}',
                        ha='right', va='center')
            st.pyplot(fig)
        
with tab3:  
    # DataFrames
    with st.expander("Learners records"):
        st.divider()
        st.write("Display All Learners Records.")
        st.dataframe(learners_df, height=300, hide_index=True)

    with st.expander("Applications Records"):
        st.divider()
        st.write("Display all applications records.")
        st.dataframe(application_df, height=300, hide_index=True, use_container_width=True)
        
    with st.expander("Work Experiences Records"):
        st.divider()
        st.write("Display all work experiences records.")
        st.dataframe(work_exp_df, height=300, hide_index=True, use_container_width=True)
        
    with st.expander("Economic Impact of Educational Attainment on Learners' Careers"):
        st.divider()
        st.write("Display the learners' average salary by their corresponding education level and employment status. Sort the output by salary in descending order.")
        avesalaryEducEmpdata, avesalaryEducEmpcolumns = fetch_avg_salary_by_education_and_emp_status()
        avesalaryEducEmpdf = pd.DataFrame(avesalaryEducEmpdata, columns=avesalaryEducEmpcolumns) 
        st.dataframe(avesalaryEducEmpdf, height=300, hide_index=True, use_container_width=True)
        
    with st.expander("Identify and Support Learners who have Limited Work Opportunities"):
        st.divider()
        st.write("Display the learner’s ID, name, age, sex, education, applied assessment, and training center. Display also the learner's salary and total work years. The salary must not exceed 60,000 and the total work years must be 3 years and below. The learner must not be currently hired in a job. Sort by average salary and total work years, both in descending order.")
        limitedWorkOppdata, limitedWorkOppcolumns = fetch_learners_with_limited_work_opp()
        limitedWorkOppdf = pd.DataFrame(limitedWorkOppdata, columns=limitedWorkOppcolumns)
        st.dataframe(limitedWorkOppdf, height=300, hide_index=True, use_container_width=True)
        
    with st.expander("Application Records Related with any Japanese Courses"):
        st.divider()
        st.write("Display applications of learners who have applied for any Japanese courses. The report should include the application's reference number, the learner's name, education level, application date, training center, and assessment title.")
        japaneseCoursedata, japaneseCoursecolumns = fetch_applications_with_japanese_courses()
        japaneseCoursedf = pd.DataFrame(japaneseCoursedata, columns=japaneseCoursecolumns)
        st.dataframe(japaneseCoursedf, height=300, hide_index=True, use_container_width=True)
    
    with st.expander("Number of Learners in Different Training Centers"):
        st.divider()
        st.write("Display the number of learners enrolled in different training centers.")
        learnersTrainingCenterdata, learnersTrainingCentercolumns = fetch_learners_in_training_centers()
        learnersTrainingCenterdf = pd.DataFrame(learnersTrainingCenterdata, columns=learnersTrainingCentercolumns)
        st.dataframe(learnersTrainingCenterdf, height=300, hide_index=True, use_container_width=True)

    with st.expander("Learners with Multiple Applications by Training Center"):
        st.divider()
        st.write("Identify learners who have applied for assessments multiple times at the same training center. This information can help TESDA understand learner engagement and possibly identify patterns or issues that lead to repeated applications. The report should include the learner's ID, name, training center, and the number of applications.")
        learnersMultipleTrainingCenterdata, learnersMultipleTrainingCentercolumns = fetch_learners_with_multiple_training_centers()
        learnersMultipleTrainingCenterdf = pd.DataFrame(learnersMultipleTrainingCenterdata, columns=learnersMultipleTrainingCentercolumns)
        st.dataframe(learnersMultipleTrainingCenterdf, height=300, hide_index=True, use_container_width=True)
        
    with st.expander("Analysis of Learners with Significant Work Experience and High Salaries in Makati-Based Training Centers Post-2020"):
        st.divider()
        st.write("Display learner’s ID, application date, name, email and the count of work experiences of applicants that have applied after 2020 and have multiple work experiences with salaries exceeding 50,000 pesos.")
        learnersSignificantWorkExpdata, learnersSignificantWorkExpcolumns = fetch_learners_with_significant_work_exp()
        learnersSignificantWorkExpdf = pd.DataFrame(learnersSignificantWorkExpdata, columns=learnersSignificantWorkExpcolumns)
        st.dataframe(learnersSignificantWorkExpdf, height=300, hide_index=True, use_container_width=True)
    
    with st.expander("Analysis of Assessments for Overseas Filipino Workers (OFWs) by Training Center"):
        st.divider()
        st.write("Display a report that shows the number of assessments taken by OFWs per training center and the number of unique assessment titles for OFWs per training center. The report should include only those training centers that have had more than three OFW assessments.")
        OFWAssessmentdata, OFWAssessmentcolumns = fetch_assessment_activities_of_OFWs()
        OFWAssessmentdf = pd.DataFrame(OFWAssessmentdata, columns=OFWAssessmentcolumns)
        st.dataframe(OFWAssessmentdf, height=300, hide_index=True, use_container_width=True)
    
    with st.expander("Identifying Learners Interested in Programming with Minimal Work Experience in Region 4-A"):
        st.divider()
        st.write("TESDA wants to identify learners who have shown an interest in programming and have minimal work experience, particularly in the Region 4-A area, which includes Cavite, Laguna, Batangas, Rizal, and Quezon. The focus is on learners who have undergone assessments related to programming during the second quarter of 2024 (April to June). The query will include details such as learners' names, age, email addresses, mobile number and total work experience.")
        learnersInterestedProgrammingdata, learnersInterestedProgrammingcolumns = fetch_learners_interested_in_programming()
        learnersInterestedProgrammingdf = pd.DataFrame(learnersInterestedProgrammingdata, columns=learnersInterestedProgrammingcolumns)
        st.dataframe(learnersInterestedProgrammingdf, height=300, hide_index=True, use_container_width=True)

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
    st.button("View Records", disabled=True, use_container_width=True)
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