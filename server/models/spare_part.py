from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class SparePart(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)  
    part_number = db.Column(db.String(100), unique=True, nullable=False)  
    category = db.Column(db.String(100), nullable=True)  # e.g., Engine, Suspension, Electrical
    price = db.Column(db.Float, nullable=False)  
    stock_quantity = db.Column(db.Integer, default=0, nullable=False) 
    image_url = db.Column(db.String(255), nullable=True)  # Path to locally stored image
    supplier_id = db.Column(db.Integer, db.ForeignKey("supplier.id"), nullable=True) 

    supplier = db.relationship("Supplier", backref="spare_parts")

    def __repr__(self):
        return f"<SparePart {self.name} - {self.part_number}>"
