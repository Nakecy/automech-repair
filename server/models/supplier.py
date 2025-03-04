from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Supplier(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False, unique=True)
    contact_email = db.Column(db.String(120), unique=True, nullable=False)
    address = db.Column(db.String(255), nullable=True)
    
    # Relationship with Spare Parts (One Supplier → Many Spare Parts)
    spare_parts = db.relationship("SparePart", backref="supplier", lazy=True)

    def __repr__(self):
        return f"<Supplier {self.name}>"
