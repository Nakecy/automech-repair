from enum import Enum
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Role(Enum):
    CUSTOMER = "customer"
    MECHANIC = "mechanic"
    ADMIN_MECHANIC = "admin_mechanic"

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    role = db.Column(db.Enum(Role), nullable=False)  # Defines if the user is a customer, mechanic, or admin mechanic

    def __repr__(self):
        return f"<User {self.name} - {self.role.value}>"
