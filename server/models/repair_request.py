from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from enum import Enum

db = SQLAlchemy()

class RequestStatus(Enum):
    PENDING = "Pending"
    IN_PROGRESS = "In Progress"
    COMPLETED = "Completed"
    CANCELED = "Canceled"

class RepairRequest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)  # Customer making the request
    mechanic_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=True)  # Assigned mechanic (if any)
    vehicle_id = db.Column(db.Integer, db.ForeignKey("vehicle.id"), nullable=False)  # Vehicle involved
    status = db.Column(db.Enum(RequestStatus), default=RequestStatus.PENDING, nullable=False)  # Repair status
    created_at = db.Column(db.DateTime, default=datetime.utcnow)  # Timestamp of request
    spare_part_id = db.Column(db.Integer, db.ForeignKey("spare_part.id"), nullable=True)  # Spare part (if matched)
    image_url = db.Column(db.String(255), nullable=True)  # Path to the uploaded image

    customer = db.relationship("User", foreign_keys=[customer_id], backref="repair_requests")
    mechanic = db.relationship("User", foreign_keys=[mechanic_id], backref="assigned_repairs")
    vehicle = db.relationship("Vehicle", backref="repair_requests")
    spare_part = db.relationship("SparePart", backref="repair_requests")

    def __repr__(self):
        return f"<RepairRequest {self.id} - {self.status.value}>"
