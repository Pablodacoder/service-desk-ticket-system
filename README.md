## Service Desk Ticketing System (Flask)

This project is a backend IT herlpdesk ticketing systems built with Flask and SQLAlchemy. It simulates how internal IT teams manage users, authenticate access, and track support tickets with role-based permissions. The system supports secure user authentication, admin-only actions, and persistent data storage using relational database

Features:
    User and admin account creation
    Secure password hashing (PBKDF2)
    Session-based authentication
    Role-based authorization (admin vs user)
    Ticket creation and tracking
    One-to-many relationship between users and tickets
    Admin-only ticket status updates
    SQLite database with SQLAlchemy ORM
    Defensive error handling (duplicate users, invalid logins)

Tech Stack:
    Backend: Python, Flask
    Database: SQLite
    ORM: SQLAlchemy
    Authentication: Werkzeug password hashing
    Environment: Python virtual environment

Security highlights:
    Passwords are never stored in plaintext
    Passwords are hashed using pbkdf2:sha256
    Session-based authentication for logged-in users
    Role-based access cvontrol to protect admin routes 
    Database-level uniqueness constraints on usernames and emails

# Clone repository
git clone https://github.com/your-username/service-desk-ticket-system.git
cd service-desk-ticket-system

# Create and activate virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install flask flask-sqlalchemy

# Run application
python3 app.py


App is available @:
http://127.0.0.1:8000

Example Routes:
/create-admin - Create an admin account
/create-user - Create a standard user 
/create-ticket - Create support ticket
/tickets - View all tickets
/Users/<id>/tickets - view tickets for a specific user
/login?username=...&password=... - Authenticate a user 

Why this Project?
Demonstrates backened fundamentals directly applicable to real-world software engineering and also my previous experience of obtaining my A+ certification

Resume Bullets:
Built a Flask-based IT helpdesk ticketing system with secure authentication, role-based authorization, and persistent data storage using SQLAlchemy.
Developed a backend service desk system simulating real-world IT ticket workflows using Python, Flask, and SQLite.
Designed relational database models supporting one-to-many user-to-ticket relationships with enforced uniqueness constraints.
