from mysql import connector
import logging
from dotenv import load_dotenv
import os

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
