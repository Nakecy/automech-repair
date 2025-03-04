from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Vehicle(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    make = db.Column(db.String(100), nullable=False)  # e.g., Toyota, Honda
    model = db.Column(db.String(100), nullable=False)  # e.g., Corolla, Civic
    year = db.Column(db.Integer, nullable=False)  # e.g., 2015
    vin = db.Column(db.String(50), unique=True, nullable=False)  # Vehicle Identification Number
    customer_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)  # Links to Customer

    customer = db.relationship("User", backref="vehicles")

    def __repr__(self):
        return f"<Vehicle {self.make} {self.model} ({self.year})>"
