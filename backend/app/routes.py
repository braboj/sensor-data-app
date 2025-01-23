from flask import Blueprint, jsonify
from markupsafe import escape
from .sensors import DiscreteSensor, AnalogSensor

main = Blueprint('main', __name__)
api = Blueprint('api', __name__, url_prefix='/api')

@main.route('/')
def home():
    return escape('Backend Home')

@api.route('/sensors', methods=['GET'])
def get_all_sensors():
    """Fetch the latest sensor data."""

    data = {
        'temperature': AnalogSensor('temperature').read(),
        'humidity': AnalogSensor('humidity').read(),
        'vibration': DiscreteSensor('vibration').read(),
    }

    return jsonify(data)