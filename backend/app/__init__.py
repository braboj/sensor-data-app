import os
import threading

from flask import Flask
from dotenv import load_dotenv
from .routes import api, main
from .database import db
from .services import SensorService

def create_app():

    # Load environment variables from .env file
    load_dotenv()

    # Configure the Flask app to use the instance folder for configuration
    app = Flask(__name__, instance_relative_config=True)

    # Load the configuration from the instance folder
    app.config.from_pyfile('config.py', silent=True)

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
        sensor_thread = threading.Thread(target=SensorService.generate_sensor_data, args=(app,))
        sensor_thread.daemon = True
        sensor_thread.start()

    return app