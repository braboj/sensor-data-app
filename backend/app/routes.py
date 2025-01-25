from flask import Blueprint, jsonify, request
from markupsafe import escape
from .services import SensorService

main = Blueprint('main', __name__)
api = Blueprint('api', __name__, url_prefix='/api')

@main.route('/')
def home():
    """Render the home page.

    Example:
        http://localhost:5000/
    """

    return escape('Backend server is running!')

@api.route('/sensors', methods=['GET'])
def get_all_sensors():
    """Fetch the latest sensor data.

    Example:
        http://localhost:5000/api/sensors?limit=10
    """

    limit = request.args.get('limit', default=100, type=int)
    data = SensorService.fetch_data(limit)
    return jsonify(data)