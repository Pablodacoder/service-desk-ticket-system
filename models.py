from flask_sqlalchemy import SQLAlchemy 
from werkzeug.security import generate_password_hash, check_password_hash 

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    role = db.Column(db.String(20), default="user") # NEW IMPLEMENTATION

    def __repr__(self):
        return f"<User {self.username} ({self.role})>"
    
    def set_password(self,password):
        #Force PBKDF2 instead of scrypt
        self.password_hash = generate_password_hash(password, 
            method="pbkdf2:sha256")

    def check_password(self,password):
        return check_password_hash(self.password_hash, password)
    
class Ticket(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text, nullable=False)
    status = db.Column(db.String(50), nullable=False, default="Open")
    priority = db.Column(db.String(50), nullable=False, default="Medium")

    #relationship
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)

    def __repr__(self):
        return f"<Ticket {self.title}>"    