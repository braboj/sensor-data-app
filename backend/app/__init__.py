import os

from flask import Flask
from .routes import api, main
from dotenv import load_dotenv

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

    return app