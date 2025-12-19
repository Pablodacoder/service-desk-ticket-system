from flask import Flask
from models import db, User, Ticket
from flask import session, request
from sqlalchemy.exc import IntegrityError
import os

app = Flask(__name__)
app.secret_key = "dev-secret-key"

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
DB_PATH = os.path.join(BASE_DIR, "service_desk.db")

print(">>> BASE_DIR:", BASE_DIR)
print(">>> DB_PATH", DB_PATH)

#Database config
app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:////{DB_PATH}"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

@app.route("/")
def home():
    return "Database connected!"

@app.route("/create-admin")
def create_admin():
    admin = User(username="admin", email="admin@example.com", role="admin")
    admin.set_password("adminpass")

    db.session.add(admin)
    db.session.commit()
    return "Admin user created!"

@app.route("/create-user")
def create_user():
    if User.query.filter_by(email="test@example.com").first():
        return "User already exists"

    user = User(username="testuser", email="test@example.com")
    user.set_password("password123")

    try:
        db.session.add(user)
        db.session.commit()
    except IntegrityError:
        db.session.rollback()
        return "User already exists"

    return "User created with password!"

@app.route("/users")
def list_users():
    users= User.query.all()
    return ",".join(u.username for u in users)

@app.route("/create-ticket")
def create_ticket():
    user = User.query.first()
   
    ticket = Ticket (
        title="Computer not turning on",
        description="Laptop does not power on when pressing the button.",
        status="Open",
        priority="High",
        user_id=user.id
    )
    db.session.add(ticket)
    db.session.commit()
    return f"Ticket {ticket.title} created for user {user.username}!"

@app.route("/tickets")
def list_tickets():
    tickets = Ticket.query.all()
    return "<br>".join(t.title for t in tickets)

@app.route("/users/<int:user_id>/tickets")
def user_tickets(user_id):
    user = User.query.get_or_404(user_id)
    tickets = Ticket.query.filter_by(user_id=user.id).all()
    return "<br>".join(t.title for t in tickets)    

@app.route("/ticket/<int:ticket_id>/status/<string:new_status>")
def update_ticket_status(ticket_id, new_status):
    ticket = Ticket.query.get_or_404(ticket_id)
    ticket.status = new_status
    db.session.commit()
    return f"Ticket {ticket.title} status updated to {new_status}!"

@app.route("/login", methods=["GET"])
def login():
    username = request.args.get("username")
    password = request.args.get("password")

    if not username or not password:
        return "Username and password required", 400

    user = User.query.filter_by(username=username).first()

    if user and user.check_password(password):
        session["user_id"] = user.id
        session["role"] = user.role
        return f"Logged in as {user.username} ({user.role})"

    return "Logged in sd admin", 401
    
if __name__ == "__main__":
    print(">>> Starting Flask server <<<")

    with app.app_context():
        db.create_all()
        print(">>> Database tables created <<<")

    app.run(host="127.0.0.1", port=8000, debug=True)