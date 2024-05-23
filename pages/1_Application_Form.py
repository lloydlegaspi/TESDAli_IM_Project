import streamlit as st
import pandas as pd
from database_manager import *

st.set_page_config(layout="wide", initial_sidebar_state="collapsed")
logo_path = "images/logo.png"

# Mapping dictionary for Assessment Status
assessment_status_mapping = {
    "Full Qualification": "FQ",
    "COC": "COC",
    "Renewal": "R"
}

# Mapping dictionary for Civil Status
civil_status_mapping = {
    "Single": "S",
    "Married": "M",
    "Widow/er": "W",
    "Separated": "SP"
}

# Mapping dictionary for Client Type
client_type_mapping = {
    "TVET Graduating Student": "TVETGS",
    "TVET graduate": "TVETG",
    "Industry worker": "IW",
    "K-12": "K-12",
    "OWF": "OWF"
}

# Mapping dictionary for Employment Status
employment_status_mapping = {
    "Casual": "C",
    "Job Order": "JO",
    "Probationary": "PR",
    "Permanent": "P",
    "Self-Employed": "SE",
    "OFW": "OFW"
}

# Custom CSS for the radio buttons
st.markdown("""
        <style>
        [role=radiogroup]{
            gap: 5rem;
        }
        </style>
        """,unsafe_allow_html=True)

col1, col2, col3 = st.columns([1, 1, 7])

with col2:
    st.image(logo_path, width=150)

with col3:
    st.markdown("<h4 style='line-height: 0.3;'>Republic of the Philippines</h4>", unsafe_allow_html=True)
    st.markdown("<h1 style='line-height: 0.6;'>TECHNICAL EDUCATION AND SKILLS DEVELOPMENT AUTHORITY</h1>", unsafe_allow_html=True)
    st.markdown("<h4 style='line-height: 0.5;'>Pangasiwaan sa Edukasyong Teknikal at Pagpapaunlad ng Kasanayan</h4>", unsafe_allow_html=True)

st.write(" ")
st.write(" ")

st.write("Please fill up completely and correctly the required information before each item below. Required items are marked with an asterisk (*).")

with st.form("application_form"):
    st.markdown("<h1 style='color: blue;'>APPLICATION FORM</h1>", unsafe_allow_html=True)
    col1, col2, col3, col4, col5 = st.columns([2, .2, 2, .2, 2])
    with col1:
        Ref_No = st.text_input("REFERENCE NUMBER*")
    with col3:
        Learners_ID = st.text_input("UNIQUE LEARNERS IDENTIFIER (ULI)*", placeholder="- - - -")
    with col5:
        Application_Date = st.date_input("Date of Application*")
        
    st.write(" ")

    with st.container(border=True):
        col1, col2 = st.columns([1, 1])
        with col1:
            Training_Center = st.text_input("Name of School/Training Center/Company")
        with col2:
            Training_Address = st.text_input("Training Center Address")

        col1, col2 = st.columns([1, 1])
        with col1:
            Assessment_Title = st.text_input("Title of Assessment Applied For")
        with col2:
            Assessment_Status = st.radio(
            "Assessment Status",
            options=["Full Qualification", "COC", "Renewal"],
            horizontal=True, index=None
        )
    
    st.write(" ")
    with st.container(border=True):
        st.markdown("<h3 style='color: blue;'>1. Client Type</h3>", unsafe_allow_html=True)
        Client_Type = st.radio(
            "Client Type",
            options=["TVET Graduating Student", "TVET graduate", "Industry worker", "K-12", "OWF"],
            horizontal=True, index=None, label_visibility="collapsed"
        )

    st.write(" ")
    with st.container(border=True):
        st.markdown("<h3 style='color: blue;'>2. Profile</h3>", unsafe_allow_html=True)
        st.write("2.1. Name")
        Name = st.text_input("Name*",
                             placeholder="First Name, Middle Name, Last Name",
                             help="Enter your full name", label_visibility="collapsed")
        
        st.write("2.2. Mailing Address")
        Address = st.text_input("Number, Street*",
                                placeholder="Number, Street, Barangay, District, City, Province, Region, Zip Code",
                                label_visibility="collapsed")
        
        col1, col2 = st.columns([1, 1])
        with col1:
            st.write("2.3. Mother's Name")
            Mothers_Name = st.text_input("Mother's Name*", label_visibility="collapsed", 
                                         placeholder="First Name, Middle Name, Last Name")
        with col2:
            st.write("2.4. Father's Name")
            Fathers_Name = st.text_input("Father's Name*", label_visibility="collapsed",
                                         placeholder="First Name, Middle Name, Last Name")


        col1, col2, col3, col4, col5, col6 = st.columns([1, 1, 1, 1, 1.5, 1])
        with col1:
            st.write("2.5. Sex")
            st.write(" ")
            Sex = st.selectbox("Sex", options=["Male", "Female"], label_visibility="collapsed", index=None)
        with col2:
            st.write("2.6. Civil Status")
            st.write(" ")
            Civil_Status = st.selectbox(
                "Civil Status",
                options=["Single", "Married", "Widow/er", "Separated"],
                label_visibility="collapsed", index=None
            )
        with col3:
            st.write("2.7. Contact Information")
            Tel_No = st.text_input("Telephone Number")
        with col4:
            st.write(" ")
            st.write(" ")
            Mobile_No = st.text_input("Mobile Number", placeholder="09xxxxxxxxx")
        with col5:
            st.write(" ")
            st.write(" ")
            Email = st.text_input("E-mail Address*")
        with col6:
            st.write(" ")
            st.write(" ")
            Fax_No = st.text_input("Fax Number")
                
        col1, col2, col3, col4, col5 = st.columns([1, 1, 1, 1.5, .5])
        with col1:
            Education = st.selectbox("2.8. Highest Educational Attainment",
                                             options=[ "Elementary Graduate", "High School Graduate", "TVET Graduate",
                                                      "College Level", "College Graduate", "Others"], index=None)
        with col2:
            Emp_Status = st.selectbox("2.9. Employment Status",
                                             options=["Casual", "Job Order", "Probationary", "Permanent", "Self-Employed", "OFW"],
                                             index=None)
        with col3:
            Birth_Date = st.date_input("2.10. Birth date", value=None)
        with col4:
            Birth_Place = st.text_input("2.11. Birth place", placeholder="City, Province")
        with col5:
            Age = st.number_input("2.12. Age", min_value=0, max_value=99, step=1)
   
    st.write(" ")
    with st.container(border=True):
        st.markdown("<h3 style='color: blue;'>3. Work Experience (National Qualification-related)</h3>", unsafe_allow_html=True)
    
    df = pd.DataFrame(
        columns=[
            "Comp_Name", "Position", "Start_Date", "End_Date", 
            "Salary", "Appt Status", "Work_Years"
        ]
    )
    edited_df = st.data_editor(df, num_rows="dynamic", use_container_width=True,
                               column_config={"Comp_Name": "3.1. Name of Company", 
                                              "Position": "3.2. Position", 
                                              "Start_Date": st.column_config.DateColumn("3.3.1. Start Date"),
                                              "End_Date": st.column_config.DateColumn("3.3.2. End Date"), 
                                              "Salary": st.column_config.NumberColumn("3.4. Monthly Salary"), 
                                              "Appt Status": st.column_config.SelectboxColumn("3.5. Appointment Status",
                                                                                               options=["Casual", "Job Order", 
                                                                                                        "Probationary", "Permanent", 
                                                                                                        "Self-Employed", "OFW"]),
                                              "Work_Years": st.column_config.NumberColumn("3.6. No. of Yrs. Working")})
    
    submit_button = st.form_submit_button("Submit")

@st.experimental_dialog("Submitted Information", width="large")
def output(Ref_No, Learners_ID, Application_Date, Training_Center, Training_Address, Assessment_Title,
           Assessment_Status, Client_Type, Name, Address, Mothers_Name, Fathers_Name, Sex, Civil_Status,
           Tel_No, Mobile_No, Email, Fax_No, Education, Emp_Status, Birth_Date, Birth_Place, Age, edited_df):
    
    Assessment_Status_Code = assessment_status_mapping[Assessment_Status]
    Client_Type_Code = client_type_mapping[Client_Type]
    Civil_Status_Code = civil_status_mapping[Civil_Status]
    Emp_Status_Code = employment_status_mapping[Emp_Status]
    Sex = 'M' if Sex == 'Male' else 'F'
    
    for index, row in edited_df.iterrows():
        row['Appt Status'] = employment_status_mapping[row['Appt Status']]
    
    st.write(f"Reference Number: {Ref_No}")
    st.write(f"Unique Learners Identifier: {Learners_ID}")
    st.write(f"Date of Application: {Application_Date}")
    st.write(f"Name of School/Training Center/Company: {Training_Center}")
    st.write(f"Training Center Address: {Training_Address}")
    st.write(f"Title of Assessment Applied For: {Assessment_Title}")
    st.write(f"Assessment Status: {Assessment_Status}")
    st.write(f"Client Type: {Client_Type}")
    st.write(f"Name: {Name}")
    st.write(f"Mailing Address: {Address}")
    st.write(f"Mother's Name: {Mothers_Name}")
    st.write(f"Father's Name: {Fathers_Name}")
    st.write(f"Sex: {Sex}")
    st.write(f"Civil Status: {Civil_Status}")
    st.write(f"Telephone Number: {Tel_No}")
    st.write(f"Mobile Number: {Mobile_No}")
    st.write(f"E-mail Address: {Email}")
    st.write(f"Fax Number: {Fax_No}")
    st.write(f"Highest Educational Attainment: {Education}")
    st.write(f"Employment Status: {Emp_Status}")
    st.write(f"Birth date: {Birth_Date}")
    st.write(f"Birth place: {Birth_Place}")
    st.write(f"Age: {Age}")
    st.write("Work Experience (National Qualification-related):")
    st.write(edited_df, use_container_width=True)
    
    confirm_button = st.button("Confirm")
    
    if confirm_button:
        # Insert data into Learners table
        insert_into_learners(Learners_ID, Client_Type_Code, Name, Address, Mothers_Name, Fathers_Name, Sex, Civil_Status_Code,
                             Tel_No, Mobile_No, Email, Fax_No, Education, Emp_Status_Code, Birth_Date, Birth_Place, Age)
        
        # Insert data into Application table
        insert_into_application(Application_Date, Training_Center, Training_Address, Assessment_Title, Assessment_Status_Code,
                                Learners_ID)
        
        # Insert data into Work_Experience table
        for index, row in edited_df.iterrows():
            comp_name = row['Comp_Name']
            position = row['Position']
            start_date = row['Start_Date']
            end_date = row['End_Date']
            salary = row['Salary']
            appt_status = row['Appt Status']
            work_years = row['Work_Years']
            insert_into_work_experience(comp_name, position, start_date, end_date, salary, appt_status, work_years, Learners_ID)
        
        st.success("Form submitted successfully!")
        
if submit_button:
    output(Ref_No, Learners_ID, Application_Date, Training_Center, Training_Address, Assessment_Title,
           Assessment_Status, Client_Type, Name, Address, Mothers_Name, Fathers_Name, Sex, Civil_Status,
           Tel_No, Mobile_No, Email, Fax_No, Education, Emp_Status, Birth_Date, Birth_Place, Age, edited_df)
    
    
     

    

