import streamlit as st
import pandas as pd
from database_manager import *
import datetime
from streamlit_extras.switch_page_button import switch_page

st.set_page_config(layout="wide", initial_sidebar_state="collapsed")
logo_path = "images/logo.png"

# Custom CSS for the button
m = st.markdown("""
    <style>
    div.stButton > button:first-child {
        background-color: #1A4793;
        color: white;
        font-size: 14px;
        font-weight: bold;
        padding: 15px 30px;
        border-radius: 5px;
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

# Custom CSS for the radio buttons
st.markdown("""
        <style>
        [role=radiogroup]{
            gap: 5rem;
        }
        </style>
        """,unsafe_allow_html=True)

col1, col2, col3 = st.columns([1, 1, 7])

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
        background: #FFFFFF; 
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
st.write(" ")

st.write("Please provide accurate and complete information for each section below. Optional fields are labeled as such.")

with st.form("application_form", clear_on_submit=True):
    st.markdown("<h1 style='color: blue;'>APPLICATION FORM</h1>", unsafe_allow_html=True)
    col1, col2= st.columns([1, 1])
    with col1:
        Learners_ID = st.text_input("UNIQUE LEARNERS IDENTIFIER (ULI)")
    with col2:
        Application_Date = st.date_input("Date of Application")
        
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
        Address = st.text_input("Number, Street",
                                placeholder="Number, Street, Barangay, District, City, Province, Region, Zip Code",
                                label_visibility="collapsed")
        
        col1, col2 = st.columns([1, 1])
        with col1:
            st.write("2.3. Mother's Name")
            Mothers_Name = st.text_input("Mother's Name", label_visibility="collapsed", 
                                         placeholder="First Name, Middle Name, Last Name")
        with col2:
            st.write("2.4. Father's Name")
            Fathers_Name = st.text_input("Father's Name", label_visibility="collapsed",
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
            Tel_No = st.text_input("Telephone Number (Optional)", placeholder="02-XXXX-YYYY")
        with col4:
            st.write(" ")
            st.write(" ")
            Mobile_No = st.text_input("Mobile Number (Optional)", placeholder="09XX-XXX-YYYY")
        with col5:
            st.write(" ")
            st.write(" ")
            Email = st.text_input("E-mail Address")
        with col6:
            st.write(" ")
            st.write(" ")
            Fax_No = st.text_input("Fax Number (Optional)", placeholder="XXXX-YYYY")
                
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
            Birth_Date = st.date_input("2.10. Birth date", value=None, min_value=datetime.date(1950, 1, 1), max_value=datetime.date(2040, 12, 31))
        with col4:
            Birth_Place = st.text_input("2.11. Birth place", placeholder="City, Province")
        with col5:
            Age = st.number_input("2.12. Age", min_value=1, max_value=99, step=1)
   
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
    
    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        submit_button = st.form_submit_button("**📥 SUBMIT**", help="Click to submit the form", use_container_width=True)

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

@st.experimental_dialog("Submitted Information", width="large")
def output(Learners_ID, Application_Date, Training_Center, Training_Address, Assessment_Title,
           Assessment_Status, Client_Type, Name, Address, Mothers_Name, Fathers_Name, Sex, Civil_Status,
           Tel_No, Mobile_No, Email, Fax_No, Education, Emp_Status, Birth_Date, Birth_Place, Age, edited_df):
   
    edited_df = edited_df.reset_index(drop=True)

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
    
    Assessment_Status_Code = assessment_status_mapping[Assessment_Status]
    Client_Type_Code = client_type_mapping[Client_Type]
    Civil_Status_Code = civil_status_mapping[Civil_Status]
    Emp_Status_Code = employment_status_mapping[Emp_Status]
    Sex = 'M' if Sex == 'Male' else 'F'
    
    edited_df['Appt Status'] = edited_df['Appt Status'].map(employment_status_mapping)
    
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
    st.write(edited_df)
    
    confirm_button = st.button("Confirm")
    
    if confirm_button:
        # Insert data into Learners table
        insert_into_learners(Learners_ID, Client_Type_Code, Name, Address, Mothers_Name, Fathers_Name, Sex, Civil_Status_Code,
                             Tel_No, Mobile_No, Email, Fax_No, Education, Emp_Status_Code, Birth_Date, Birth_Place, Age)
        
        # Insert data into Application table
        insert_into_application(Application_Date, Training_Center, Training_Address, Assessment_Title, Assessment_Status_Code,
                                Learners_ID)
        
        # Insert data into Work_Experience table
        if not edited_df.empty:
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
    output(Learners_ID, Application_Date, Training_Center, Training_Address, Assessment_Title,
           Assessment_Status, Client_Type, Name, Address, Mothers_Name, Fathers_Name, Sex, Civil_Status,
           Tel_No, Mobile_No, Email, Fax_No, Education, Emp_Status, Birth_Date, Birth_Place, Age, edited_df)

def render_footer():
    st.markdown("""
    <style>
    .footer {
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
        background-color: #253C64; /* Background color */
        color: #FFFFFF; /* Text color */
        text-align: center;
        font-size: 12px; /* Font size */
        padding: 30px;
        border-radius: 10px;
        margin-top: 30px;
    }
    </style>
    <div class="footer">
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
    

