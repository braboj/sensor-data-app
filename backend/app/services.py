from .models import SensorData
from .database import db
from .sensors import AnalogSensor, DiscreteSensor
import time


class SensorService(object):
    """Service class for handling sensor data."""

    @staticmethod
    def generate_data(app):
        """Thread to generate sensor data and store it in the database."""

        # Create the simulated field sensors
        temperature = AnalogSensor('temperature')
        humidity = AnalogSensor('humidity')
        vibration = DiscreteSensor('vibration')

        # Thread loop
        while True:

            # Sample time is fixed to 10 seconds
            time.sleep(10)

            # Map the readings to the database model
            sensor_data = SensorData(
                temperature=temperature.read(),
                humidity=humidity.read(),
                vibration=vibration.read()
            )

            # Store the readings in the database
            with app.app_context():
                db.session.add(sensor_data)
                db.session.commit()

    @staticmethod
    def fetch_data(limit=100):
        """Get the latest sensor data from the database."""

        # Get the required amount of sensor readings
        data = SensorData.query.order_by(
            SensorData.timestamp.desc()
        ).limit(limit).all()

        # Return the data in json format
        return [
            {
                "id": entry.id,
                "timestamp": entry.timestamp,
                "temperature": entry.temperature,
                "humidity": entry.humidity,
                "vibration": entry.vibration
            } for entry in data
        ]
