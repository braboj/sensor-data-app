from flask import Blueprint
from markupsafe import escape

main = Blueprint('main', __name__)
api = Blueprint('api', __name__, url_prefix='/api')

@main.route('/')
def home():
    return escape('Backend Home')

@api.route('/sensors', methods=['GET'])
def get_all_sensors():
    """Fetch the latest sensor data."""
    return escape('Sensor Data')