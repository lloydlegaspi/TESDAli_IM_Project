from mysql import connector
import logging
from dotenv import load_dotenv
import os
import matplotlib.pyplot as plt
import pandas as pd

load_dotenv()
PASSWORD = os.getenv("PASSWORD")

@staticmethod
# Connect to the MySQL database
def connect_to_database():
    try:
        conn = connector.connect(
            host="localhost",
            user="root",
            password=PASSWORD,
            database="db_infoman"
        )
        logging.info("Connection established")
        return conn
    except connector.Error as e:
        print(f"Error connecting to MySQL database: {e}")
        return None

# Create tables in the database
def create_tables():
    try:
        conn = connect_to_database()
        if conn:
            cursor = conn.cursor()
            # Create Learners table
            cursor.execute("""
            CREATE TABLE IF NOT EXISTS Learners (
                Learners_ID INT PRIMARY KEY,
                Client_Type VARCHAR(6) NOT NULL CHECK (Client_Type IN ('TVETGS', 'TVETG', 'IW', 'K-12', 'OWF')),
                Name VARCHAR(50) NOT NULL,
                Address VARCHAR(100) NOT NULL,
                Mothers_Name VARCHAR(50) NOT NULL,
                Fathers_Name VARCHAR(50) NOT NULL,
                Sex CHAR(1) NOT NULL CHECK (Sex IN ('M', 'F')),
                Civil_Status VARCHAR(2) NOT NULL CHECK (Civil_Status IN ('S', 'M', 'W', 'SP')),
                Tel_No VARCHAR(12) DEFAULT 'N/A',
                Mobile_No VARCHAR(13) DEFAULT 'N/A',
                Email VARCHAR(25) NOT NULL,
                Fax_No VARCHAR(9) DEFAULT 'N/A',
                Education VARCHAR(30) NOT NULL,
                Emp_Status VARCHAR(3) NOT NULL CHECK (Emp_Status IN ('C', 'JO', 'PR', 'P', 'SE', 'OFW')),
                Birth_Date DATE NOT NULL,
                Birth_Place VARCHAR(50) NOT NULL,
                Age INT NOT NULL
            )
            """)
            # Create Application table
            cursor.execute("""
            CREATE TABLE IF NOT EXISTS Application (
                Ref_No INT AUTO_INCREMENT PRIMARY KEY,
                Application_Date DATE NOT NULL,
                Training_Center VARCHAR(80) NOT NULL,
                Training_Address VARCHAR(100) NOT NULL,
                Assessment_Title VARCHAR(50) NOT NULL,
                Assessment_Status VARCHAR(3) NOT NULL CHECK (Assessment_Status IN ('FQ', 'COC', 'R')),
                Learners_ID INT,
                FOREIGN KEY (Learners_ID) REFERENCES Learners(Learners_ID)
                    ON UPDATE CASCADE
                    ON DELETE SET NULL
            )
            """)
            # Create Work_Exp table
            cursor.execute("""
            CREATE TABLE IF NOT EXISTS Work_Exp (
                Work_Exp_Code INT AUTO_INCREMENT PRIMARY KEY,
                Comp_Name VARCHAR(80) NOT NULL,
                Position VARCHAR(50) NOT NULL,
                Start_Date DATE NOT NULL,
                End_Date DATE NOT NULL,
                Salary DECIMAL(8, 2) NOT NULL,
                Appt_Status VARCHAR(3) NOT NULL CHECK (Appt_Status IN ('C', 'JO', 'PR', 'P', 'SE', 'OFW')),
                Work_Years INT NOT NULL,
                Learners_ID INT NOT NULL,
                FOREIGN KEY (Learners_ID) REFERENCES Learners(Learners_ID)
                    ON UPDATE CASCADE
                    ON DELETE CASCADE
            )
            """)
            print("Tables created successfully")
    except connector.Error as e:
        print(f"Error creating tables: {e}")
    finally:
        if conn:
            conn.close()

# INSERT RECORDS
# Insert data into the Learners table
def insert_into_learners(learners_id, client_type, name, address, mothers_name, fathers_name, sex, civil_status,
                         tel_no, mobile_no, email, fax_no, education, emp_status, birth_date, birth_place, age):
    try:
        conn = connect_to_database()
        if conn:
            cursor = conn.cursor()
            insert_query = """
            INSERT INTO Learners 
            (Learners_ID, Client_Type, Name, Address, Mothers_Name, Fathers_Name, Sex, Civil_Status, Tel_No, Mobile_No, Email, 
            Fax_No, Education, Emp_Status, Birth_Date, Birth_Place, Age) 
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """
            learner_data = (learners_id, client_type, name, address, mothers_name, fathers_name, sex, civil_status,
                            tel_no, mobile_no, email, fax_no, education, emp_status, birth_date, birth_place, age)
            cursor.execute(insert_query, learner_data)
            conn.commit()
            print("Data inserted into Learners table successfully")
    except connector.Error as e:
        print(f"Error inserting data into Learners table: {e}")
    finally:
        if conn:
            conn.close()

# Insert data into the Application table
def insert_into_application(application_date, training_center, training_address, assessment_title, assessment_status,
                            learners_id):
    try:
        conn = connect_to_database()
        if conn:
            cursor = conn.cursor()
            insert_query = """
            INSERT INTO Application 
            (Application_Date, Training_Center, Training_Address, Assessment_Title, Assessment_Status, Learners_ID) 
            VALUES (%s, %s, %s, %s, %s, %s)
            """
            application_data = (application_date, training_center, training_address, assessment_title, assessment_status,
                                learners_id)
            cursor.execute(insert_query, application_data)
            conn.commit()
            print("Data inserted into Application table successfully")
    except connector.Error as e:
        print(f"Error inserting data into Application table: {e}")
    finally:
        if conn:
            conn.close()

# Insert data into the Work_Experience table
def insert_into_work_experience(comp_name, position, start_date, end_date, salary, appt_status, work_years, learners_id):
    try:
        conn = connect_to_database()
        if conn:
            cursor = conn.cursor()
            insert_query = """
            INSERT INTO Work_Exp 
            (Comp_Name, Position, Start_Date, End_Date, Salary, Appt_Status, Work_Years, Learners_ID) 
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            """
            work_exp_data = (comp_name, position, start_date, end_date, salary, appt_status, work_years, learners_id)
            cursor.execute(insert_query, work_exp_data)
            conn.commit()
            print("Data inserted into Work_Experience table successfully")
    except connector.Error as e:
        print(f"Error inserting data into Work_Experience table: {e}")
    finally:
        if conn:
            conn.close()

# UPDATE RECORDS
def update_record(table, record_id, update_data):
    primary_keys = {
        "Learners": "Learners_ID",
        "Application": "Ref_No",
        "Work_Exp": "Work_Exp_Code"
    }
    
    if table not in primary_keys:
        print(f"Unknown table: {table}")
        return None, None
    
    primary_key = primary_keys[table]
    
    try:
        conn = connect_to_database()
        if conn:
            cursor = conn.cursor()
            set_clause = ", ".join([f"{key} = %s" for key in update_data.keys()])
            values = list(update_data.values())
            update_query = f"UPDATE {table} SET {set_clause} WHERE {primary_key} = %s"
            values.append(record_id)
            cursor.execute(update_query, values)
            conn.commit()
            print(f"Record in {table} table updated successfully")
    except connector.Error as e:
        print(f"Error updating record in {table} table: {e}")
    finally:
        if conn:
            conn.close()

# DELETE RECORDS  
def delete_record(table, record_id):
    try:
        conn = connect_to_database()
        if conn:
            cursor = conn.cursor()
            primary_key = {
                "Learners": "Learners_ID",
                "Application": "Ref_No",
                "Work_Exp": "Work_Exp_Code"
            }.get(table)
            if not primary_key:
                raise ValueError("Invalid table name")
            
            cursor.execute(f"DELETE FROM {table} WHERE {primary_key} = %s", (record_id,))
            conn.commit()
            
            if cursor.rowcount == 0:
                return False, f"No record found with ID {record_id} in {table} table"
            return True, f"Record with ID {record_id} deleted from {table} table successfully"
    except connector.Error as e:
        return False, f"Error deleting record from {table} table: {e}"
    finally:
        if conn:
            conn.close()
            
# FETCH/READ RECORDS
def fetch_learners():
    try:
        conn = connect_to_database()
        if conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM Learners")
            result = cursor.fetchall()
            columns = cursor.column_names
            cursor.close()
            return result, columns
    except connector.Error as e:
        print(f"Error fetching data from Learners table: {e}")
    finally:
        if conn:
            conn.close()

def fetch_applications():
    try:
        conn = connect_to_database()
        if conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM Application")
            result = cursor.fetchall()
            columns = cursor.column_names
            cursor.close()
            return result, columns
    except connector.Error as e:
        print(f"Error fetching data from Application table: {e}")
    finally:
        if conn:
            conn.close()

def fetch_work_experiences():
    try:
        conn = connect_to_database()
        if conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM Work_Exp")
            result = cursor.fetchall()
            columns = cursor.column_names
            cursor.close()
            return result, columns
    except connector.Error as e:
        print(f"Error fetching data from Work_Exp table: {e}")
    finally:
        if conn:
            conn.close()

#FETCH RECORD BY ID         
def fetch_record(table, record_id):
    primary_keys = {
        "Learners": "Learners_ID",
        "Application": "Ref_No",
        "Work_Exp": "Work_Exp_Code"
    }
    
    if table not in primary_keys:
        print(f"Unknown table: {table}")
        return None, None
    
    primary_key = primary_keys[table]
    
    try:
        conn = connect_to_database()
        if conn:
            cursor = conn.cursor()
            query = f"SELECT * FROM {table} WHERE {primary_key} = %s"
            cursor.execute(query, (record_id,))
            result = cursor.fetchone()
            if result:
                columns = [desc[0] for desc in cursor.description]
                cursor.close()
                return result, columns
            else:
                return None, None
    except connector.Error as e:
        print(f"Error fetching record from {table} table: {e}")
        return None, None
    finally:
        if conn:
            conn.close()

#View Page Functions
def fetch_metrics():
    try:
        conn = connect_to_database()
        if conn:
            cursor = conn.cursor()
            
            cursor.execute("SELECT COUNT(DISTINCT Assessment_Title) FROM Application")
            courses_offered = cursor.fetchone()[0]

            cursor.execute("SELECT COUNT(*) FROM Learners")
            total_learners = cursor.fetchone()[0]

            cursor.execute("SELECT COUNT(*) FROM Application")
            total_applications = cursor.fetchone()[0]

            cursor.execute("SELECT AVG(Age) FROM Learners")
            average_age = round(cursor.fetchone()[0] or 0)

            cursor.close()
            return courses_offered, total_learners, total_applications, average_age
            
    except connector.Error as e:
        print(f"Error fetching metrics from database: {e}")
    finally:
        if conn:
            conn.close()


# Application Summary
def fetch_assessment_titles_distribution():
    try:
        conn = connect_to_database()
        if conn:
            cursor = conn.cursor()
            cursor.execute("""
            SELECT Assessment_Title, COUNT(*) AS Count
            FROM Application
            GROUP BY Assessment_Title
            """)
            result = cursor.fetchall()
            cursor.close()
            return result

    except connector.Error as e:
        print(f"Error fetching assessment titles distribution: {e}")
    finally:
        if conn:
            conn.close()

def fetch_top_training_centers():
    try:
        conn = connect_to_database()
        if conn:
            cursor = conn.cursor()
            cursor.execute("""
            SELECT Training_Center, COUNT(*) AS Count
            FROM Application
            GROUP BY Training_Center
            ORDER BY Count DESC
            """)
            result = cursor.fetchall()
            cursor.close()
            return result

    except connector.Error as e:
        print(f"Error fetching top training centers: {e}")
    finally:
        if conn:
            conn.close()

def fetch_assessment_status_distribution():
    try:
        conn = connect_to_database()
        if conn:
            cursor = conn.cursor()
            cursor.execute("""
            SELECT 
                CASE 
                    WHEN Assessment_Status = 'FQ' THEN 'Full Qualification'
                    WHEN Assessment_Status = 'COC' THEN 'Certificate of Competency'
                    WHEN Assessment_Status = 'R' THEN 'Renewal'
                END AS Assessment_Status,
                COUNT(*) AS Count
            FROM Application
            GROUP BY Assessment_Status
            ORDER BY Count DESC
            """)
            result = cursor.fetchall()
            cursor.close()
            return result 
    except connector.Error as e:
        print(f"Error fetching assessment status distribution: {e}")
        return None
    finally:
        if conn:
            conn.close()

def fetch_applications_over_time():
    try:
        conn = connect_to_database()
        if conn:
            cursor = conn.cursor()
            cursor.execute("""
            SELECT YEAR(Application_Date) AS Year, COUNT(*) AS Count
            FROM Application
            GROUP BY YEAR(Application_Date)
            ORDER BY Year
            """)
            result = cursor.fetchall()
            cursor.close()
            return result
    except connector.Error as e:
        print(f"Error fetching applications over time: {e}")
        return None

# Learners Summary
def fetch_client_type_distribution():
    try:
        conn = connect_to_database()
        if conn:
            cursor = conn.cursor()
            cursor.execute("""
            SELECT 
                CASE 
                    WHEN Client_Type = 'TVETGS' THEN 'TVET Graduating Student'
                    WHEN Client_Type = 'TVETG' THEN 'TVET Graduate'
                    WHEN Client_Type = 'IW' THEN 'Industry Worker'
                    WHEN Client_Type = 'K-12' THEN 'K-12'
                    WHEN Client_Type = 'OWF' THEN 'OWF'
                END AS Client_Type,
                COUNT(*) AS Count
            FROM Learners
            GROUP BY Client_Type
            """)
            result = cursor.fetchall()
            cursor.close()
            return result
    except connector.Error as e:
        print(f"Error fetching client type distribution: {e}")
    finally:
        if conn:
            conn.close()
    
def fetch_age_distribution():
    try:
        conn = connect_to_database()
        if conn:
            cursor = conn.cursor()
            cursor.execute("""
            SELECT Age, COUNT(*) AS Count
            FROM Learners
            GROUP BY Age
            ORDER BY Age
            """)
            result = cursor.fetchall()
            cursor.close()
            return result
    except connector.Error as e:
        print(f"Error fetching age distribution: {e}")
    finally:
        if conn:
            conn.close()

def fetch_sex_distribution():
    try:
        conn = connect_to_database()
        if conn:
            cursor = conn.cursor()
            cursor.execute("""
            SELECT Sex, COUNT(*) AS Count
            FROM Learners
            GROUP BY Sex
            """)
            result = cursor.fetchall()
            cursor.close()
            return result
    except connector.Error as e:
        print(f"Error fetching sex distribution: {e}")
    finally:
        if conn:
            conn.close()

def fetch_avg_salary_by_emp_status():
    try:
        conn = connect_to_database()
        if conn:
            cursor = conn.cursor()
            query = """
            SELECT
                Emp_Status,
                AVG(Salary) AS 'Average Salary'
            FROM
                learners l, work_exp w
            WHERE
                l.Learners_ID = w.Learners_ID
            GROUP BY
                Emp_Status
            ORDER BY
                AVG(Salary) ASC
            """
            cursor.execute(query)
            result = cursor.fetchall()
            cursor.close()
            return result
    except connector.Error as e:
        print(f"Error fetching average salary data: {e}")
        return []
    finally:
        if conn:
            conn.close()

#Generated Reports
# Easy
def fetch_applicants_with_managerial_positions():
    try:
        conn = connect_to_database()
        if conn:
            cursor = conn.cursor()
            cursor.execute("""
            SELECT 
                Learners_ID, Position, Work_Years, Salary
            FROM 
                work_exp
            WHERE 
                Position LIKE '%Manager%'AND Work_Years >= 3
            ORDER BY
                Salary DESC;

            """)
            result = cursor.fetchall()
            columns = cursor.column_names
            cursor.close()
            return result, columns
    except connector.Error as e:
        print(f"Error fetching applicants with managerial positions: {e}")
        return []
    finally:
        if conn:
            conn.close()
            
def fetch_industry_workers_in_CALABARZON():
    try:
        conn = connect_to_database()
        if conn:
            cursor = conn.cursor()
            cursor.execute("""
            SELECT Name, Age, Address, Mobile_No, Email
            FROM Learners
            WHERE (Address LIKE '%Cavite%' OR Address LIKE '%Laguna%' OR Address LIKE '%Batangas%' OR Address LIKE '%Rizal%' OR Address LIKE '%Quezon%')
            AND Client_Type = 'IW'
            ORDER BY Name;
            """)
            result = cursor.fetchall()
            columns = cursor.column_names
            cursor.close()
            return result, columns
    except connector.Error as e:
        print(f"Error fetching industry workers in CALABARZON: {e}")
        return []
    finally:
        if conn:
            conn.close()

def fetch_manila_high_school_graduates():
    try:
        conn = connect_to_database()
        if conn:
            cursor = conn.cursor()
            cursor.execute("""
            SELECT Name, Age
            FROM learners
            WHERE Address LIKE '%Manila%' AND Education = 'High School Graduate' 
            ORDER BY Age DESC;
            """)
            result = cursor.fetchall()
            columns = cursor.column_names
            cursor.close()
            return result, columns
    except connector.Error as e:
        print(f"Error fetching Manila high school graduates: {e}")
        return []
    finally:
        if conn:
            conn.close()

# Moderate
def fetch_applicants_demographics_per_client_type():
    try:
        conn = connect_to_database()
        if conn:
            cursor = conn.cursor()
            cursor.execute("""
            SELECT 
                Client_Type,
                Sex,
                COUNT(*) AS Number_Of_Learners,
                AVG(Age) AS Average_Age
            FROM 
                Learners
            WHERE 
                Age >= 18 AND Civil_Status = 'S'
            GROUP BY 
                Client_Type, 
                Sex
            HAVING 
                COUNT(*) > 1
            ORDER BY 
                Client_Type,  
                Average_Age DESC;
            """)
            result = cursor.fetchall()
            columns = cursor.column_names
            cursor.close()
            return result, columns
    except connector.Error as e:
        print(f"Error fetching applicants demographics per client type: {e}")
        return []
    finally:
        if conn:
            conn.close()


def fetch_applications_programming_networking():
    try:
        conn = connect_to_database()
        if conn:
            cursor = conn.cursor()
            cursor.execute("""
            SELECT 
                Training_Center,
                Assessment_Title,
                COUNT(Ref_No) AS Total_Applications
            FROM 
                application
            WHERE 
                YEAR(Application_Date) = 2024 AND MONTH(Application_Date) BETWEEN 04 AND 06
                AND (Assessment_Title LIKE '%Programming%' OR Assessment_Title LIKE '%Networking%')
            GROUP BY 
                Training_Center, Assessment_Title
            HAVING 
                COUNT(Ref_No) >= 2
            ORDER BY 
                Total_Applications DESC;
            """)
            result = cursor.fetchall()
            columns = cursor.column_names
            cursor.close()
            return result, columns
    except connector.Error as e:
        print(f"Error fetching applications: {e}")
        return []
    finally:
        if conn:
            conn.close()


def fetch_lc_by_p_se_empstatus():
    try:
        conn = connect_to_database()
        if conn:
            cursor = conn.cursor()
            cursor.execute("""
            SELECT 
                Emp_Status,
                COUNT(*) AS 'Learner Count'
            FROM 
                learners
            WHERE 
                Emp_Status = 'P' OR Emp_Status = 'SE'
            GROUP BY 
                Emp_Status
            HAVING 
                COUNT(*) > 1
            ORDER BY 
                COUNT(*) ASC;
            """)
            result = cursor.fetchall()
            columns = cursor.column_names
            cursor.close()
            return result, columns
    except connector.Error as e:
        print(f"Error fetching average salary data: {e}")
        return []
    finally:
        if conn:
            conn.close()

def fetch_training_centers_with_multiple_assessment_titles():
    try:
        conn = connect_to_database()
        if conn:
            cursor = conn.cursor()
            cursor.execute("""
            SELECT Training_Center, Training_Address, COUNT(DISTINCT(Assessment_Title)) AS 'Assessment Count'
            FROM application
            WHERE YEAR(Application_Date) >= 2020 AND (Training_Address LIKE '%Manila%' OR Training_Address LIKE '%Makati%')
            GROUP BY Training_Center, Training_Address
            HAVING COUNT(Assessment_Title) > 1
            ORDER BY Training_Center;
            """)
            result = cursor.fetchall()
            columns = cursor.column_names
            cursor.close()
            return result, columns
    except connector.Error as e:
        print(f"Error fetching training centers with multiple assessment titles: {e}")
        return []
    finally:
        if conn:
            conn.close()
                
# Difficult
def fetch_learners_with_limited_work_opp():
    try:
        conn = connect_to_database()
        if conn:
            cursor = conn.cursor()
            cursor.execute("""
            SELECT 
                l.Learners_ID,
                l.Name,
                l.Age,
                l.Sex,
                l.Education,
                a.Assessment_Title,
                a.Training_Center,
                AVG(w.Salary) AS Avg_Salary,
                SUM(w.Work_Years) AS Total_Work_Years
            FROM 
                application a, learners l, work_exp w
            WHERE 
                l.Learners_ID = a.Learners_ID 
                AND l.Learners_ID = w.Learners_ID 
                AND (w.End_Date IS NULL OR w.End_Date <= CURDATE())
            GROUP BY 
                l.Learners_ID, 
                l.Name, 
                l.Age, 
                l.Sex, 
                l.Education, 
                a.Assessment_Title, 
                a.Training_Center
            HAVING 
                Avg_Salary <= 60000 AND
                Total_Work_Years <= 3
            ORDER BY 
                Avg_Salary DESC, 
                Total_Work_Years DESC;
            """)
            result = cursor.fetchall()
            columns = cursor.column_names
            cursor.close()
            return result, columns
    except connector.Error as e:
        print(f"Error fetching learners who have limited work opportunites: {e}")
        return []
    finally:
        if conn:
            conn.close()

def fetch_assessment_activities_of_OFWs():
    try:
        conn = connect_to_database()
        if conn:
            cursor = conn.cursor()
            cursor.execute("""
            SELECT
                a.Training_Center,
                COUNT(a.Ref_No) AS Total_Assessments,
                COUNT(DISTINCT a.Assessment_Title) AS Unique_Assessment_Titles
            FROM
                application a, learners l 
            WHERE 
                a.Learners_ID = l.Learners_ID
            AND
                l.Emp_Status = 'OFW'
            GROUP BY
                a.Training_Center
            HAVING
                COUNT(a.Ref_No) > 3
            ORDER BY Total_Assessments DESC, Unique_Assessment_Titles DESC;
            """)
            result = cursor.fetchall()
            columns = cursor.column_names
            cursor.close()
            return result, columns
    except connector.Error as e:
        print(f"Error fetching assessment activities of OFWs: {e}")
        return []
    finally:
        if conn:
            conn.close()
            
def fetch_learners_with_significant_work_exp():
    try:
        conn = connect_to_database()
        if conn:
            cursor = conn.cursor()
            cursor.execute("""
            SELECT a.Learners_ID, a.Application_Date, l.Name, l.Email, COUNT(w.Work_Exp_Code) AS 'Work Experience', AVG(w.Salary) AS 'Average Salary'
            FROM learners AS l, application AS a, work_exp AS w
            WHERE l.Learners_ID = a.Learners_ID AND l.Learners_ID = w.Learners_ID AND YEAR(a.Application_Date) > 2018 AND a.Training_Address LIKE '%Makati%'
            GROUP BY  a.Learners_ID, a.Application_Date, l.Name, l.Email
            HAVING COUNT(w.Work_Exp_Code)  > 1 AND AVG(w.Salary) > 50000
            ORDER BY COUNT(w.Work_Exp_Code) DESC;
            """)
            result = cursor.fetchall()
            columns = cursor.column_names
            cursor.close()
            return result, columns
    except connector.Error as e:
        print(f"Error fetching learners with significant work experience: {e}")
        return []
    finally:
        if conn:
            conn.close()

if __name__ == "__main__":
    pass
