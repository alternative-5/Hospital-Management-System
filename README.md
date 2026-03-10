Hospital Management System (Django)

A Hospital Management System built using the Django web framework to manage hospital operations such as patient records, doctor management, appointment scheduling, and billing. This system helps reduce manual work and improves efficiency in hospital administration.


Features

-  Doctor Management
-  Patient Management
-  Appointment Booking System
-  Medical Records Management
-  Billing Management
-  User Authentication (Admin / Doctor / Patient)
-  Dashboard for Admin
-  Database Storage using SQLite/MySQL

Technologies Used

Backend: Python, Django
Frontend: HTML, CSS, Bootstrap, JavaScript
Database: SQLite / MySQL
Version Control: Git & GitHub



Project Structure


hospital_management/
│
├── hospital_management/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── app/
│   ├── models.py
│   ├── views.py
│   ├── admin.py
│   ├── urls.py
│   └── templates/
│
├── db.sqlite3
├── manage.py
└── requirements.txt


Installation

Follow these steps to run the project locally.

1.Clone the Repository

bash
git clone https://github.com/alternative-5/Hospital-Management-System


2.Navigate to Project Folder

bash
cd hospital-management-system


3.Create Virtual Environment

bash
python -m venv venv


4.Activate Virtual Environment

-Windows
bash
venv\Scripts\activate


-Mac/Linux
bash
source venv/bin/activate


5.Install Dependencies

bash
pip install -r requirements.txt


6.Run Migrations

bash
python manage.py migrate


7.Create Superuser

bash
python manage.py createsuperuser


8.Run Server

bash
python manage.py runserver


9.Open browser and go to:


http://127.0.0.1:8000/


10.Admin Panel

Access Django admin panel:


http://127.0.0.1:8000/admin


Login using the superuser credentials created earlier.


Screenshots

Add screenshots of your project here.

Example:

screenshots
    Dashboard.png
    appointment.png
    patient_list.png


Future Improvements

- Online payment integration
- Email notifications for appointments
- Doctor availability tracking
- Patient medical history analytics
- REST API using Django REST Framework


Author

Vaibhav Maliwad

GitHub: https://github.com/alternative-5

License

This project is open-source and developed for educational pursposes. You may modify and use it with proper attribution.
