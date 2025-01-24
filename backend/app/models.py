from .database import db

class SensorData(db.Model):
    """Basic sensor data model with temperature, humidity, and vibration."""

    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime, default=db.func.current_timestamp())
    temperature = db.Column(db.Float, nullable=False)
    humidity = db.Column(db.Float, nullable=False)
    vibration = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"<SensorData id={self.id} timestamp={self.timestamp}>"