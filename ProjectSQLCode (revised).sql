-- Table for Learners
CREATE TABLE Learners (
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
);

-- Table for Applications
CREATE TABLE Application (
    Ref_No INT PRIMARY KEY AUTO_INCREMENT,
    Application_Date DATE NOT NULL,
    Training_Center VARCHAR(80) NOT NULL,
    Training_Address VARCHAR(100) NOT NULL,
    Assessment_Title VARCHAR(50) NOT NULL,
    Assessment_Status VARCHAR(3) NOT NULL CHECK (Assessment_Status IN ('FQ', 'COC', 'R')),
    Learners_ID INT,
    FOREIGN KEY (Learners_ID) REFERENCES Learners(Learners_ID)
                    ON UPDATE CASCADE
                    ON DELETE SET NULL
);

-- Table for Work Experience
CREATE TABLE Work_Exp (
    Work_Exp_Code INT PRIMARY KEY AUTO_INCREMENT,
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
);

INSERT INTO Learners (
    Learners_ID, Client_Type, Name, Address, Mothers_Name, Fathers_Name, Sex, Civil_Status,
    Tel_No, Mobile_No, Email, Fax_No, Education, Emp_Status, Birth_Date, Birth_Place, Age
) VALUES
    (1, 'IW', 'Juan Manuel Santos', '4418 Dallas Street, Barangay San Antonio, Makati City, Metro Manila, NCR, 1226',
     'Maria M. Santos', 'Jose B. Santos', 'M', 'M', '02-8123-4567', '0912-345-6789', 'juanmanuel@gmail.com', '8123-4567',
     'College Graduate', 'P', '1988-05-15', '123 Sesame Street, Quezon City', 35),

    (2, 'IW', 'Miguel Cruz', '4418 Dallas Street, Barangay San Antonio, Makati City, Metro Manila, NCR, 1226',
     'Maricel F. Cruz', 'Robert Cruz', 'M', 'S', '02-6152-4491', '0942-265-3297', 'miguelcruz@gmail.com', '3283-6659',
     'College Graduate', 'C', '2000-02-08', '64 Mabini Street, Marikina City', 24),

    (3, 'OWF', 'Mariella Pascual Garcia', '24 Cruzada, Barangay Zenia, Dasmariñas, Cavite, 4114',
     'Rosalie P. Garcia', 'Nestor D. Garcia', 'F', 'S', '82-9928-2384', '0936-153-9274', 'mariellagarcia@gmail.com', '8275-7235',
     'College Graduate', 'OFW', '1997-07-14', '21 Mileguas Dasmarinas, Cavite', 26),

    (4, 'K-12', 'Abby Santiago Mendoza', '519 Santol Street, Manila, Metro Manila, NCR, 1008',
     'Marites Q. dela Cruz', 'Pedro A. Alonte', 'F', 'S', '02-4345-3422', '0917-432-2234', 'abbysantiago@yahoo.com', '8123-4324',
     'High School Graduate', 'SE', '2000-02-15', '24 Bluemintritt Street, Manila', 24),

    (5, 'K-12', 'Aeron Eulin Ronquillo', '31 M. Perez, St., Poblacion, Norzagaray, Bulacan, 3013',
     'Marilyn E. Ronquillo', 'Filipe B. Ronquillo', 'M', 'S', '02-8777-4584', '0917-123-4567', 'aeron@gmail.com', '5667-9865',
     'College Level', 'SE', '1992-10-03', 'Norzagaray, Bulacan', 32);



INSERT INTO application (
    Ref_No, Application_Date, Training_Center, Training_Address, Assessment_Title, Assessment_Status, Learners_ID
) VALUES
    (1, '2024-04-03', 'ABE International Business College-Makati, Inc.', '#95 Gil Puyat Ave., Brgy. Palanan, Makati City', 'Bread and Pastry Production NC II', 'FQ', 1),

    (2, '2024-04-03', 'ABE International Business College-Makati, Inc.', '#95 Gil Puyat Ave., Brgy. Palanan, Makati City', 'Bread and Pastry Production NC II', 'FQ', 2),

    (3, '2024-04-05', 'Gonbee Nihongo Kyoiku Inc.', '37 J.P. Rizal Street, Tubuan II, Silang, Cavite', 'Japanese Language and Culture I', 'COC', 3),

    (4, '2024-05-02', 'Gonbee Nihongo Kyoiku Inc.', '37 J.P. Rizal Street, Tubuan II, Silang, Cavite', 'Japanese Language and Culture II', 'COC', 3),

    (5, '2024-06-02', 'Joysis Tech Voc Inc.', '1 Inda Maria St., Potrero, Malabon', 'Java Programming NC III', 'R', 4),

    (6, '2024-06-01', 'Lucky 8 Norzagaray Training Center', '0845 Quintana Bldg, 2nd and 3rd Floor, Partida, Norzagaray, Bulacan, Philippines', 'Cookery NCII', 'R', 5);


INSERT INTO work_exp (
    Work_Exp_Code, Comp_Name, Position, Start_Date, End_Date, Salary, Appt_Status, Work_Years, Learners_ID
) VALUES
    (1, 'PayMongo Philippines, Inc.', 'Associate Project Manager', '2020-06-14', '2029-08-12', 90465.19, 'P', 3, 1),

    (2, 'Philippine Airlines, Incorporated', 'Senior Web Developer', '2013-10-01', '2020-07-06', 50242.28, 'P', 7, 1),

    (3, 'Insular Oil Corporation', 'Junior Web Developer', '2009-06-04', '2013-12-28', 18550.67, 'P', 4, 1),

    (4, 'PayMongo Philippines, Inc.', 'Lead Software Engineer', '2024-03-01', '2026-08-08', 42567.23, 'C', 0, 2),

    (5, 'Monde Nissin Corporation', 'Software Engineer', '2022-04-18', '2023-12-29', 29457.93, 'P', 1, 2),

    (6, 'Coo & Riku Co Ltd', 'Sales Manager', '2023-03-20', '2027-04-02', 98235.36, 'JO', 1, 3),

    (7, 'Don Quijote Co., Ltd.', 'Junior Accountant', '2019-08-07', '2023-03-01', 64912.77, 'P', 3, 3),

    (8, 'Coo & Riku Co Ltd', 'Sales Manager', '2023-03-20', '2030-02-16', 98235.36, 'JO', 1, 3),

    (9, 'Don Quijote Co., Ltd.', 'Junior Accountant', '2019-08-07', '2023-03-01', 64912.77, 'P', 3, 3),

    (10, 'Jolibee Food Corp', 'Food Service Crew', '2019-04-23', '2019-12-23', 12300.35, 'C', 0, 4),

    (11, 'McDonalds Corp', 'Cashier', '2023-09-21', '2024-02-21', 15200.21, 'C', 0, 4),

    (12, 'PayMongo Philippines, Inc.', 'Senior Marketing Researcher', '2017-03-01', '2023-03-31', 40000.00, 'P', 6, 5),

    (13, 'PayMongo Philippines, Inc.', 'Marketing Assistant', '2012-03-04', '2016-12-20', 17500.00, 'P', 4, 5);
    
INSERT INTO learners (Learners_ID, Client_Type, Name, Address, Mothers_Name, Fathers_Name, Sex, Civil_Status, Tel_No, Mobile_No, Email, Fax_No, Education, Emp_Status, Birth_Date, Birth_Place, Age)
VALUES
(6, 'OWF', 'Juan Dela Cruz', '123 Main St', 'Maria Cruz', 'Jose Cruz', 'M', 'S', '1234567890', '0987654321', 'juan@example.com', '123456789', 'College', 'OFW', '1980-01-01', 'Manila', 40),
(7, 'OWF', 'Maria Clara', '456 Elm St', 'Ana Clara', 'Pedro Clara', 'F', 'M', '1231231234', '0980980980', 'maria@example.com', '987654321', 'High School', 'OFW', '1985-05-15', 'Cebu', 35),
(8, 'OWF', 'Pedro Santos', '789 Maple Ave', 'Juana Santos', 'Carlos Santos', 'M', 'M', '3213213210', '8768768765', 'pedro@example.com', '321654987', 'College', 'OFW', '1975-07-20', 'Davao', 45),
(9, 'OWF', 'Luisa Gomez', '101 Pine St', 'Elena Gomez', 'Miguel Gomez', 'F', 'S', '6546546540', '7657657654', 'luisa@example.com', '654987321', 'College', 'OFW', '1990-10-10', 'Cagayan de Oro', 30),
(10, 'OWF', 'Carlos Reyes', '202 Oak St', 'Rosa Reyes', 'Juan Reyes', 'M', 'M', '9879879870', '6546546543', 'carlos@example.com', '987321654', 'College', 'OFW', '1982-03-15', 'Quezon City', 38);

INSERT INTO application (Application_Date, Training_Center, Training_Address, Assessment_Title, Assessment_Status, Learners_ID)
VALUES
-- TESDA Training Center 1
('2023-01-01', 'TESDA Training Center 1', '123 Training St', 'Welding', 'FQ', 6),
('2023-01-02', 'TESDA Training Center 1', '123 Training St', 'Carpentry', 'COC', 6),
('2023-02-01', 'TESDA Training Center 1', '123 Training St', 'Plumbing', 'FQ', 6),
('2023-03-01', 'TESDA Training Center 1', '123 Training St', 'Electrician', 'FQ', 7),
('2023-04-01', 'TESDA Training Center 1', '123 Training St', 'Welding', 'R', 7),
-- TESDA Training Center 2
('2023-01-03', 'TESDA Training Center 2', '456 Training Ave', 'Welding', 'FQ', 8),
('2023-02-03', 'TESDA Training Center 2', '456 Training Ave', 'Carpentry', 'COC', 8),
('2023-03-03', 'TESDA Training Center 2', '456 Training Ave', 'Plumbing', 'FQ', 8),
('2023-04-03', 'TESDA Training Center 2', '456 Training Ave', 'Electrician', 'R', 9),
('2023-05-03', 'TESDA Training Center 2', '456 Training Ave', 'Masonry', 'FQ', 9),
-- TESDA Training Center 3
('2023-06-01', 'TESDA Training Center 3', '789 Training Blvd', 'Welding', 'FQ', 10),
('2023-07-01', 'TESDA Training Center 3', '789 Training Blvd', 'Carpentry', 'COC', 10),
('2023-08-01', 'TESDA Training Center 3', '789 Training Blvd', 'Plumbing', 'FQ', 10),
('2023-09-01', 'TESDA Training Center 3', '789 Training Blvd', 'Electrician', 'R', 6),
('2023-10-01', 'TESDA Training Center 3', '789 Training Blvd', 'Masonry', 'FQ', 6),
-- TESDA Training Center 4
('2023-11-01', 'TESDA Training Center 4', '1010 Training Dr', 'Welding', 'FQ', 7),
('2023-12-01', 'TESDA Training Center 4', '1010 Training Dr', 'Carpentry', 'COC', 7),
('2023-01-15', 'TESDA Training Center 4', '1010 Training Dr', 'Plumbing', 'FQ', 8),
('2023-02-15', 'TESDA Training Center 4', '1010 Training Dr', 'Electrician', 'R', 9),
('2023-03-15', 'TESDA Training Center 4', '1010 Training Dr', 'Masonry', 'FQ', 10);

-- Insert sample data into learners table starting from Learners_ID 11
INSERT INTO learners (Learners_ID, Client_Type, Name, Address, Mothers_Name, Fathers_Name, Sex, Civil_Status, Tel_No, Mobile_No, Email, Fax_No, Education, Emp_Status, Birth_Date, Birth_Place, Age)
VALUES
(11, 'TVETGS', 'Juan Dela Cruz', '123 Main St, Cavite', 'Maria Cruz', 'Jose Cruz', 'M', 'S', '1234567890', '0987654321', 'juan@example.com', '123456789', 'High School', 'P', '1990-01-01', 'Cavite', 34),
(12, 'TVETG', 'Maria Clara', '456 Elm St, Laguna', 'Ana Clara', 'Pedro Clara', 'F', 'M', '1231231234', '0980980980', 'maria@example.com', '987654321', 'High School', 'P', '1995-05-15', 'Laguna', 29),
(13, 'IW', 'Pedro Santos', '789 Maple Ave, Batangas', 'Juana Santos', 'Carlos Santos', 'M', 'M', '3213213210', '8768768765', 'pedro@example.com', '321654987', 'High School', 'P', '1985-07-20', 'Batangas', 39),
(14, 'K-12', 'Luisa Gomez', '101 Pine St, Rizal', 'Elena Gomez', 'Miguel Gomez', 'F', 'S', '6546546540', '7657657654', 'luisa@example.com', '654987321', 'High School', 'P', '2000-10-10', 'Rizal', 24),
(15, 'OWF', 'Carlos Reyes', '202 Oak St, Quezon', 'Rosa Reyes', 'Juan Reyes', 'M', 'M', '9879879870', '6546546543', 'carlos@example.com', '987321654', 'High School', 'P', '1982-03-15', 'Quezon', 42);

-- Insert sample data into application table
INSERT INTO application (Application_Date, Training_Center, Training_Address, Assessment_Title, Assessment_Status, Learners_ID)
VALUES
('2024-01-01', 'TESDA Training Center 1', '123 Training St, Cavite', 'Programming Basics', 'FQ', 11),
('2024-02-01', 'TESDA Training Center 2', '456 Training Ave, Laguna', 'Java Programming', 'COC', 11),
('2024-04-01', 'TESDA Training Center 3', '789 Training Blvd, Batangas', 'Python Programming', 'FQ', 12),
('2024-04-15', 'TESDA Training Center 1', '123 Training St, Cavite', 'Programming Basics', 'FQ', 13),
('2024-05-01', 'TESDA Training Center 2', '456 Training Ave, Laguna', 'Java Programming', 'COC', 14),
('2024-07-25', 'TESDA Training Center 2', '456 Training Ave, Quezon', 'JavaScript Programming', 'FQ', 15);

-- Insert sample data into work_exp table
INSERT INTO work_exp (Comp_Name, Position, Start_Date, End_Date, Salary, Appt_Status, Work_Years, Learners_ID)
VALUES
('ABC Company', 'Programmer', '2023-01-01', '2024-01-01', 50000.00, 'P', 1, 12),
('XYZ Corporation', 'Software Engineer', '2022-06-01', '2023-06-01', 60000.00, 'P', 1, 12),
('123 Solutions', 'Web Developer', '2022-03-01', '2023-03-01', 55000.00, 'P', 1, 13),
('Tech Solutions', 'Java Developer', '2022-02-01', '2023-02-01', 65000.00, 'P', 1, 14),
('Mobile Apps Inc.', 'Python Developer', '2022-04-01', '2023-04-01', 70000.00, 'P', 1, 15);