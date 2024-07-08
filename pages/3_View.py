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

st.write(" ")
# Example usage of displaying metrics (assuming you use streamlit)
col1, col2, col3, col4, col5 = st.columns([3, 1, 1, 1, 1])
col1.markdown("<h1 style='color: blue; text-align: center;'>TESDA Dashboard</h1>", unsafe_allow_html=True)
col2.metric("Courses Offered", courses_offered, "Assessments")
col3.metric("Current Learners", total_learners, "Learners")
col4.metric("Total Applications", total_applications, "Applications")
col5.metric("Learners' Average Age", average_age)

st.write(" ")

tab1, tab2, tab3 = st.tabs(["Application Summary", "Learners' Profile", "Generated Reports"])

# Application Summary
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
                plt.xlabel('No. of Applications')
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

                plt.figure(figsize=(10, 6.6))
                bars = plt.barh(df['Training Center'], df['Count'], color='skyblue')
                plt.xlabel('No. of Applications')
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
            plt.ylabel('No. of Applications')
            plt.yticks(range(0, max(df['Count']) + 1, 1))
            plt.tight_layout()
            st.pyplot(plt)
        
    with col2:
        st.subheader("Applications Over Years")
        data = fetch_applications_over_time()

        if data:
            df = pd.DataFrame(data, columns=['Year', 'Count'])
            df['Year'] = pd.to_datetime(df['Year'], format='%Y')
            df.set_index('Year', inplace=True)

            # Plotting with Matplotlib
            plt.figure(figsize=(10, 6))
            years = [row[0] for row in data] 
            counts = [row[1] for row in data]
            plt.plot(years, counts, marker='o', linestyle='-')
            plt.xlabel('Year')
            plt.ylabel('No. of Applications')
            plt.xticks(years)
            plt.yticks(range(0, max(df['Count']) + 1, 1))
            plt.tight_layout()

            # Display the plot using Streamlit
            st.pyplot()
            
        st.write(" ")
        st.write(" ")


# Learners' Profile
with tab2:
    col1, col2 = st.columns(2)

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
                width=620,
                height=620
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
    
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Sex Distribution")
        sex_data = fetch_sex_distribution()

        if sex_data:
            sex_df = pd.DataFrame(sex_data, columns=['Sex', 'Count'])
            blues = ['skyblue', '##31b1e0'] 
            
            # Plotting Sex Distribution with Plotly
            fig = go.Figure(data=[go.Pie(labels=sex_df['Sex'], values=sex_df['Count'], hole=0.2, 
                                         marker=dict(colors=blues))])
            fig.update_traces(textposition='inside', textinfo='label+percent', showlegend=False)
            fig.update_layout(
                width=620,
                height=620
            )
            st.plotly_chart(fig)
            
    with col2:
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
    # General Reports
    st.write("**General Reports**")
    with st.expander("Learners records"):
        st.divider()
        st.write("Display All Learners Records.")
        st.dataframe(learners_df, hide_index=True)

    with st.expander("Applications Records"):
        st.divider()
        st.write("Display all applications records.")
        st.dataframe(application_df, hide_index=True, use_container_width=True)
        
    with st.expander("Work Experiences Records"):
        st.divider()
        st.write("Display all work experiences records.")
        st.dataframe(work_exp_df, hide_index=True, use_container_width=True)
    
    
    # Basic Reports
    st.write("**Basic Reports**")
    with st.expander("1. Identification of Applicants with Managerial Positions for Mentorship Opportunity"):
        st.divider()
        st.write("The assessors seek to identify applicants with managerial experience for mentoring roles in a new upcoming course on resource management. The report should display each learner’s ID, position, years spent working, and salary. Only include those who have held a managerial position for at least 3 years. Sort the data by salary, from highest to lowest.")
        managerialApplicantsdata, managerialApplicantscolumns = fetch_applicants_with_managerial_positions()
        managerialApplicantsdf = pd.DataFrame(managerialApplicantsdata, columns=managerialApplicantscolumns)
        st.dataframe(managerialApplicantsdf, hide_index=True, use_container_width=True)
        
    with st.expander("2. Identification of Industry Workers in CALABARZON Region"):
        st.divider()
        st.write("The Technical Education and Skills Development Authority (TESDA) wants to identify industry workers (Client_Type = 'IW') located in the CALABARZON region (Cavite, Laguna, Batangas, Rizal, Quezon). They require a report listing the names, ages, addresses, mobile numbers, and email addresses of these industry workers, sorted alphabetically by name.")
        industryWorkersdata, industryWorkerscolumns = fetch_industry_workers_in_CALABARZON()
        industryWorkersdf = pd.DataFrame(industryWorkersdata, columns=industryWorkerscolumns)
        st.dataframe(industryWorkersdf, hide_index=True, use_container_width=True)
    
    with st.expander("3. Identification of TESDA applicants Who Live in Manila and are High School Graduates. "):
        st.divider()
        st.write("TESDA aims to determine the applicants who live in Manila and are high school graduates as their highest educational attainment. Sort them by age in descending order. ")
        manilaHighSchoolGraduatesdata, manilaHighSchoolGraduatescolumns = fetch_manila_high_school_graduates()
        manilaHighSchoolGraduatesdf = pd.DataFrame(manilaHighSchoolGraduatesdata, columns=manilaHighSchoolGraduatescolumns)
        st.dataframe(manilaHighSchoolGraduatesdf, hide_index=True, use_container_width=True)
    
    # Medium Reports
    st.write("**Medium Reports**")
    
    with st.expander("1. Overview of Applicants’ Demographics Per Client Type"):
        st.divider()
        st.write("The assessors need an overview of the applicants' demographics. The report should display the total number of learners and their average age, categorized by client type and sex. Only include learners who are of legal age, civil status is single, and the result should be at least one or more learners. Sort the results alphabetically by client type and then by average age in descending order.")
        applicantsDemographicsdata, applicantsDemographicscolumns = fetch_applicants_demographics_per_client_type()
        applicantsDemographicsdf = pd.DataFrame(applicantsDemographicsdata, columns=applicantsDemographicscolumns)
        st.dataframe(applicantsDemographicsdf, hide_index=True, use_container_width=True)
        
    with st.expander("2. Analysis of Training Centers with High Application Numbers for Programming and Networking Assessments"):
        st.divider()
        st.write("The Technical Education and Skills Development Authority (TESDA) wants to analyze training centers that have received significant numbers of applications for programming and networking assessments between April and June 2024. They require a report listing the training centers, assessment titles, and total application counts, focusing on those centers with at least two applications. Results should be sorted in descending order based on the total number of applications.")
        application_programming_networking_data, application_programming_networking_cols = fetch_applications_programming_networking()
        application_programming_networking_df = pd.DataFrame(application_programming_networking_data, columns=application_programming_networking_cols)
        st.dataframe(application_programming_networking_df, hide_index=True, use_container_width=True)
    
    with st.expander("3. Employment Status with Average Salary Greater than 50000"):
        st.divider()
        st.write("TESDA wants to analyze the average salary of learners based on their employment status. The assessors need a report that shows the average salary of learners, grouped by their employment status having only an average salary greater than 50000, and sorts the results by average. Display each learner's employment status and average salary in ascending order.")
        avesalaryEmpdata, avesalaryEmpcolumns = fetch_avg_salary_emp_status()
        avesalaryEmpdf = pd.DataFrame(avesalaryEmpdata, columns=avesalaryEmpcolumns) 
        st.dataframe(avesalaryEmpdf, hide_index=True, use_container_width=True)
    
    with st.expander("4. Analysis of TESDA Training Centers that Offers More Than One Assessment Title Since the Year 2020"):
        st.divider()
        st.write("TESDA aims to determine which training center offers more than 1 assessment title starting from the year 2020, and located in Manila or Makati. The report should display the training center's name, address, and the number of unique assessment titles offered. Sort the results by the training center's name.")
        trainingCentersdata, trainingCenterscolumns = fetch_training_centers_with_multiple_assessment_titles()
        trainingCentersdf = pd.DataFrame(trainingCentersdata, columns=trainingCenterscolumns)
        st.dataframe(trainingCentersdf, hide_index=True, use_container_width=True)

    # Advanced Reports
    st.write("**Advanced Reports**")
    
    with st.expander("1. Assessing the New Qualification System for Learners Selection"):
        st.divider()
        st.write("TESDA is planning to introduce a new qualification system to identify and support learners who have limited work opportunities. Make a report that would display the learner’s ID, name, age, sex, education, applied assessment, and training center. Display also the learner's salary and total work years. The salary must be lower than 60,000 and the total work years must be 3 years and below. The learner must not be currently hired in a job. Sort by average salary and total work years, both in descending order.")
        limitedWorkOppdata, limitedWorkOppcolumns = fetch_learners_with_limited_work_opp()
        limitedWorkOppdf = pd.DataFrame(limitedWorkOppdata, columns=limitedWorkOppcolumns)
        st.dataframe(limitedWorkOppdf, hide_index=True, use_container_width=True)
        
    with st.expander("2. Analysis of Assessments for Overseas Filipino Workers (OFWs) by Training Center"):
        st.divider()
        st.write("Display a report that shows the number of assessments taken by OFWs per training center and the number of unique assessment titles for OFWs per training center. The report should include only those training centers that have had more than three OFW assessments. Sort the results by the number of assessments and unique assessment title in descending order.")
        OFWAssessmentdata, OFWAssessmentcolumns = fetch_assessment_activities_of_OFWs()
        OFWAssessmentdf = pd.DataFrame(OFWAssessmentdata, columns=OFWAssessmentcolumns)
        st.dataframe(OFWAssessmentdf, hide_index=True, use_container_width=True)
        
    with st.expander("3. Analysis of Learners with Significant Work Experience and High Salaries in Makati-Based Training Centers Post-2018"):
        st.divider()
        st.write("Display learner’s ID, application date, name, email and the count of work experiences of applicants that have applied after 2018 and have multiple work experiences with salaries exceeding 50,000 pesos. Sort by the count of work experiences in descending order.")
        learnersSignificantWorkExpdata, learnersSignificantWorkExpcolumns = fetch_learners_with_significant_work_exp()
        learnersSignificantWorkExpdf = pd.DataFrame(learnersSignificantWorkExpdata, columns=learnersSignificantWorkExpcolumns)
        st.dataframe(learnersSignificantWorkExpdf, hide_index=True, use_container_width=True)
   
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
        padding-top: 2rem;  
        padding-left: 5rem; 
        padding-right: 5rem; 
        padding-bottom: 0rem; 
    }
    </style>
"""
st.markdown(hide_streamlit_bar, unsafe_allow_html=True)