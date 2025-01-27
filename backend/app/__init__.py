import os
import threading
from flask import Flask
from .routes import api, main
from .database import db
from .services import SensorService

def create_app(test_config=None):

    # Configure the Flask app to use the instance folder for configuration
    app = Flask(__name__, instance_relative_config=True)

    # Load the default configuration
    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)

    # Load the test configuration
    else:
        app.config.from_mapping(test_config)

    # Register the routes with the app
    app.register_blueprint(main)
    app.register_blueprint(api)

    # Initialize the database
    db.init_app(app)

    # Create the database tables
    with app.app_context():
        db.create_all()

    # Start the sensor data generation thread
    with app.app_context():
        sensor_thread = threading.Thread(
            target=SensorService.generate_data,
            args=(app,)
        )
        sensor_thread.daemon = True
        sensor_thread.start()

    return app