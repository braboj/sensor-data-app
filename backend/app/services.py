from .models import SensorData
from .database import db
from .sensors import AnalogSensor, DiscreteSensor
import time


class SensorService(object):

    @staticmethod
    def generate_sensor_data(app):

        temperature = AnalogSensor('temperature')
        humidity = AnalogSensor('humidity')
        vibration = DiscreteSensor('vibration')

        while True:
            sensor_data = SensorData(
                temperature=temperature.read(),
                humidity=humidity.read(),
                vibration=vibration.read()
            )

            with app.app_context():
                db.session.add(sensor_data)
                db.session.commit()

            time.sleep(10)

    @staticmethod
    def get_sensor_data(limit=100):

        data = SensorData.query.order_by(
            SensorData.timestamp.desc()
        ).limit(limit).all()

        return [
            {
                "id": entry.id,
                "timestamp": entry.timestamp,
                "temperature": entry.temperature,
                "humidity": entry.humidity,
                "vibration": entry.vibration
            } for entry in data
        ]
