# TESDAli: A Streamlined TESDA Assessment Application Management System

Faculty of the College of Computer and Information Sciences, Polytechnic University of the Philippines, Sta. Mesa, Manila
In partial fulfillment of the course COMP 010: Information Management

Presented by:  
Doria, Chynna Mae V.  
Macaraeg, Paul Angelo O.  
Legaspi, John Lloyd S.  
Valoria, Kyla Mae N.  

April, 2024  

## OVERVIEW OF THE PROJECT

TESDA is the government agency tasked with overseeing technical vocational education and training. This project aims to develop a web-based application form and a database system to streamline TESDA Assessments Application Forms. This form is a requisite document for candidates seeking Assessment and Certification for their TESDA-completed training, particularly new applicants. Notably, this form is crucial not only for initial applications but also for candidates renewing or revalidating their National Certificate (NC) issued by their training institution. The form collects various information from applicants, including personal details, training details, and work experience.

### Business Rules

1. Each learner is assigned a unique learner ID, which remains consistent across all their assessment applications.
2. Every TESDA Competency Assessment application form must be associated with one learner, and each learner can be linked to one or more application forms.
3. Learners must provide at least one active email address for correspondence and announcement purposes.
4. Learners have the option to include multiple work experiences, with each work experience being tied to a specific learner. It is also possible for a learner to have no work experience recorded.

**Disclaimer**: The form provided for this project was revised and includes solely the first page of the original document. It does not represent the official form being used by TESDA.

## Technologies Used

- **Python**: The primary programming language used.
- **Streamlit**: The main framework used to build the web application
- **MySQL**: Database engine for storing and managing application data.
- **Pandas**: For handling and displaying tabular data.

## Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/your-username/tesdali.git
   cd tesdali
   ```
2. Create a virtual environment and activate it:
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
3. Install the required packages:
   ```sh
   pip install -r requirements.txt
   ```

## Usage

1. Run the Streamlit application:
   ```sh
   streamlit run app.py
   ```
2. Open your web browser and navigate to http://localhost:8501 to view the application.

## Project Structure
```bash
tesdali/
│
├── database_manager.py   # Database management functions
├── app.py                # Main Streamlit application
├── requirements.txt      # Required Python packages
├── images/
│   └── logo.png          # Logo image used in the application
└── README.md             # Project README file
```

## Database

The application uses a MySQL database to store the form data. The database schema includes the following tables:

**Learners**: Stores personal and contact details of the applicants.
**Application**: Stores application-specific details.
**Work_Exp**: Stores work experience related to the national qualifications

Each table's schema is defined in the database_manager.py file.

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch (git checkout -b feature-branch).
3. Make your changes.
4. Commit your changes (git commit -m 'Add new feature').
5. Push to the branch (git push origin feature-branch).
6. Open a Pull Request.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.

## Acknowledgements

We would like to thank the Faculty of the College of Computer and Information Sciences at the Polytechnic University of the Philippines for their guidance and support throughout this project.
