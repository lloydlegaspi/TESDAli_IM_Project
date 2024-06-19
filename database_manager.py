from mysql import connector
import logging
from dotenv import load_dotenv
import os
import matplotlib.pyplot as plt
import pandas as pd

load_dotenv()
PASSWORD = os.getenv("PASSWORD")

@staticmethod
# Function to connect to the MySQL database
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

# Function to create tables in the database
def create_tables():
    try:
        conn = connect_to_database()
        if conn:
            cursor = conn.cursor()
            # Create Learners table
            cursor.execute("""
            CREATE TABLE IF NOT EXISTS Learners (
                Learners_ID INT PRIMARY KEY,
                Client_Type VARCHAR(6) NOT NULL,
                Name VARCHAR(50) NOT NULL,
                Address VARCHAR(100) NOT NULL,
                Mothers_Name VARCHAR(50) NOT NULL,
                Fathers_Name VARCHAR(50) NOT NULL,
                Sex CHAR(1) NOT NULL,
                Civil_Status VARCHAR(2) NOT NULL,
                Tel_No VARCHAR(12) DEFAULT 'N/A',
                Mobile_No VARCHAR(13) DEFAULT 'N/A',
                Email VARCHAR(25) NOT NULL,
                Fax_No VARCHAR(9) DEFAULT 'N/A',
                Education VARCHAR(30) NOT NULL,
                Emp_Status VARCHAR(3) NOT NULL,
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
                Assessment_Status VARCHAR(3) NOT NULL,
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
                Appt_Status VARCHAR(3) NOT NULL,
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


# Function to insert data into the Learners table
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

# Function to insert data into the Application table
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

# Function to insert data into the Work_Experience table
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
            
# Functions to fetch data from the database
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

def fetch_metrics():
    try:
        conn = connect_to_database()
        if conn:
            cursor = conn.cursor()
            
            # Fetch Courses Offered count
            cursor.execute("SELECT COUNT(DISTINCT Assessment_Title) FROM Application")
            courses_offered = cursor.fetchone()[0]

            # Fetch Total Learners count
            cursor.execute("SELECT COUNT(*) FROM Learners")
            total_learners = cursor.fetchone()[0]

            # Fetch Total Applications count
            cursor.execute("SELECT COUNT(*) FROM Application")
            total_applications = cursor.fetchone()[0]

            # Fetch Average Age of Learners
            cursor.execute("SELECT AVG(Age) FROM Learners")
            average_age = round(cursor.fetchone()[0] or 0)

            cursor.close()
            return courses_offered, total_learners, total_applications, average_age
            
    except connector.Error as e:
        print(f"Error fetching metrics from database: {e}")
    finally:
        if conn:
            conn.close()

# Function to fetch assessment titles distribution and visualize (new)
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

# Function to fetch top training centers and visualize (new)
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

# Function to fetch applications over time from the database
def fetch_applications_over_time():
    try:
        conn = connect_to_database()
        if conn:
            cursor = conn.cursor()
            cursor.execute("""
            SELECT MONTH(Application_Date) AS Month, COUNT(*) AS Count
            FROM Application
            GROUP BY MONTH(Application_Date)
            ORDER BY Month
            """)
            result = cursor.fetchall()
            cursor.close()
            return result
    except connector.Error as e:
        print(f"Error fetching applications over time: {e}")
        return None

# Function to update data in the Learners table
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

def fetch_client_type_distribution():
    try:
        conn = connect_to_database()
        if conn:
            cursor = conn.cursor()
            cursor.execute("""
            SELECT 
                CASE 
                    WHEN Client_Type = 'TVETGS' THEN 'TVET Graduating Student'
                    WHEN Client_Type = 'TVETG' THEN 'TVET graduate'
                    WHEN Client_Type = 'IW' THEN 'Industry worker'
                    WHEN Client_Type = 'K-12' THEN 'K-12'
                    WHEN Client_Type = 'OFW' THEN 'Overseas Filipino Worker'
                    ELSE 'Other'
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
    
# Function to fetch age distribution
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

# Function to fetch sex distribution
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
            
def fetch_avg_salary_by_education_and_emp_status():
    try:
        conn = connect_to_database()
        if conn:
            cursor = conn.cursor()
            cursor.execute("""
            SELECT
                l.Education, 
                l.Emp_Status, 
                AVG(w.Salary) AS Avg_Salary
            FROM
                learners l, work_exp w
            WHERE
                l.Learners_ID = w.Learners_ID
            GROUP BY 
                l.Education, 
                l.Emp_Status
            ORDER BY 
                Avg_Salary DESC
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
            
def fetch_applications_with_japanese_courses():
    try:
        conn = connect_to_database()
        if conn:
            cursor = conn.cursor()
            cursor.execute("""
            SELECT
                a.Ref_No,
                l.Name AS 'Learner Name',
                l.Education,
                a.Application_Date,
                a.Training_Center,
                a.Assessment_Title
            FROM
                application a,
                learners l
            WHERE
                a.Learners_ID = l.Learners_ID
                AND Assessment_Title LIKE '%Japanese%'
            ORDER BY
                l.Name,
                a.Application_Date;
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

def fetch_learners_in_training_centers():
    try:
        conn = connect_to_database()
        if conn:
            cursor = conn.cursor()
            cursor.execute("""
            SELECT Training_Center, COUNT(DISTINCT Learners_ID) AS 'Applicant Count'
            FROM application AS a
            GROUP BY a.Training_Center;

            """)
            result = cursor.fetchall()
            columns = cursor.column_names
            cursor.close()
            return result, columns
    except connector.Error as e:
        print(f"Error fetching training centers: {e}")
        return []
    finally:
        if conn:
            conn.close()

def fetch_learners_with_multiple_training_centers():
    try:
        conn = connect_to_database()
        if conn:
            cursor = conn.cursor()
            cursor.execute("""
            SELECT l.Learners_ID, l.Name, a.Training_Center, COUNT(a.Training_Center) AS 'Application Count'
            FROM learners AS l, application AS a
            WHERE l.Learners_ID = a.Learners_ID
            GROUP BY l.Learners_ID, l.Name, a.Training_Center
            HAVING COUNT(A.Training_Center) > 1;
            """)
            result = cursor.fetchall()
            columns = cursor.column_names
            cursor.close()
            return result, columns
    except connector.Error as e:
        print(f"Error fetching learners with multiple training centers: {e}")
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
            SELECT a.Learners_ID, a.Application_Date, l.Name, l.Email, COUNT(w.Work_Exp_Code) AS 'Work Experience'
            FROM learners AS l, application AS a, work_exp AS w
            WHERE l.Learners_ID = a.Learners_ID AND l.Learners_ID = w.Learners_ID AND YEAR(a.Application_Date) > 2020 AND a.Training_Address LIKE '%Makati%' AND w.Salary > 50000
            GROUP BY  a.Learners_ID, a.Application_Date, l.Name, l.Email
            HAVING COUNT(w.Work_Exp_Code)  > 1 ;

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
                COUNT(a.Ref_No) > 3;
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

def fetch_learners_interested_in_programming():
    try:
        conn = connect_to_database()
        if conn:
            cursor = conn.cursor()
            cursor.execute("""
            SELECT
                l.Learners_ID,
                l.Name,
                l.Age,
                l.Email,
                l.Mobile_No,
                SUM(w.Work_Years) AS Total_Work_Years
            FROM
                learners l, application a, work_exp w
            WHERE l.Learners_ID = a.Learners_ID AND l.Learners_ID = w.Learners_ID
            AND
                (a.Training_Address LIKE '%Cavite' OR
                a.Training_Address LIKE '%Laguna' OR
                a.Training_Address LIKE '%Batangas' OR
                a.Training_Address LIKE '%Rizal' OR
                a.Training_Address LIKE '%Quezon')
            AND l.Education NOT LIKE '%College%'
            AND a.Assessment_Title LIKE '%Programming%'
            AND YEAR(Application_Date) = 2024 AND MONTH(Application_Date) BETWEEN 04 AND 06
            GROUP BY
                l.Learners_ID, l.Name, l.Age, l.Email, l.Mobile_No
            HAVING Total_Work_Years <= 1
            ORDER BY
                l.Name;
            """)
            result = cursor.fetchall()
            columns = cursor.column_names
            cursor.close()
            return result, columns
    except connector.Error as e:
        print(f"Error fetching learners interested in programming: {e}")
        return []
    finally:
        if conn:
            conn.close()

# Function to delete a record from the specified table
def delete_record(table, record_id):
    try:
        conn = connect_to_database()
        if conn:
            cursor = conn.cursor()
            # Determine the primary key column based on the table name
            primary_key = {
                "Learners": "Learners_ID",
                "Application": "Ref_No",
                "Work_Exp": "Work_Exp_Code"
            }.get(table)
            if not primary_key:
                raise ValueError("Invalid table name")
            # Delete the record
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

if __name__ == "__main__":
    pass
