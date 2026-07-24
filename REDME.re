#  Job Application Tracker

A Django-based web application to manage and track job applications efficiently. Users can add, update, view, and delete job applications while monitoring their application status through a simple dashboard.

---

##  Project Overview

Job Application Tracker helps job seekers organize all their job applications in one place. It provides CRUD functionality, a dashboard with application statistics, and a clean Bootstrap-based user interface.

---

##  Features

-  Home Dashboard
-  Add New Job Application
-  View All Applications
-  Update Existing Application
- Delete Application (Confirmation Page)
-  View Application Details
-  Dashboard Statistics
-  Form Validation
-  Success Messages
-  Bootstrap 5 Responsive Design
-  Django ModelForm Validation
-  Custom Request Logger Middleware
-  Django Admin Panel

---

##  Technologies Used

- Python 3
- Django 6
- SQLite3
- HTML5
- CSS3
- Bootstrap 5

---

##  Project Structure

```
job_tracker/
│
├── job_tracker/
│ ├── settings.py
│ ├── urls.py
│ ├── wsgi.py
│ └── asgi.py
│
├── jobs/
│ ├── admin.py
│ ├── forms.py
│ ├── middleware.py
│ ├── models.py
│ ├── urls.py
│ ├── views.py
│ └── migrations/
│
├── templates/
│ ├── base.html
│ ├── navbar.html
│ ├── footer.html
│ ├── home.html
│ └── jobs/
│ ├── list.html
│ ├── create.html
│ ├── update.html
│ ├── delete.html
│ └── detail.html
│
├── static/
│ ├── css/
│ └── js/
│
├── db.sqlite3
├── manage.py
└── README.md
```

---

##  Dashboard

The home page displays:

- Total Applications
- Applied
- Interview
- Offer
- Accepted
- Rejected

---

##  Job Application Fields

| Field | Type |
|-------|------|
| Company Name | CharField |
| Position | CharField |
| Job Location | CharField |
| Salary | DecimalField |
| Status | ChoiceField |
| Application Date | DateField |
| Deadline | DateField |
| Notes | TextField |
| Created At | DateTimeField |
| Updated At | DateTimeField |

---

##  Validation Rules

- Company Name is required
- Position is required
- Salary cannot be negative
- Deadline cannot be earlier than Application Date
- Notes cannot exceed 500 characters

---

##  URL Routes

| URL | Description |
|------|-------------|
| / | Home Dashboard |
| /jobs/ | View All Applications |
| /jobs/add/ | Add Application |
| /jobs/<id>/ | Application Details |
| /jobs/<id>/edit/ | Update Application |
| /jobs/<id>/delete/ | Delete Application |

---

##  Installation

### Clone the repository

```bash
git clone <repository-url>
```

### Move to project directory

```bash
cd job_tracker
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

#### Windows

```bash
venv\Scripts\activate
```

#### Linux / macOS

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install django
```

### Apply Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### Create Superuser

```bash
python manage.py createsuperuser
```

### Run the Server

```bash
python manage.py runserver
```

Visit:

```
http://127.0.0.1:8000/
```

---

##  Admin Panel

```
http://127.0.0.1:8000/admin/
```

Login using the superuser credentials.

---

##  Custom Middleware

The project includes a custom middleware named **RequestLoggerMiddleware**.

It logs:

- Current Date & Time
- HTTP Method
- Requested URL

Example:

```
---------------------------------
Time : 2026-07-25 10:45 AM
Method : GET
Path : /jobs/
---------------------------------
```

---

##  Future Improvements

- User Authentication
- Search Applications
- Filter by Status
- Pagination
- Email Notifications
- File Upload (Resume)
- Company Logo Support

---

##  Developed By

**Md Baized sheikh**

Diploma in Computer Science & Technology

Faridpur Polytechnic Institute

---

##  License

This project is developed for educational purposes.