from flask import Flask
from .routes import api, main

def create_app():

    # Configure the Flask app to use the instance folder for configuration
    app = Flask(__name__, instance_relative_config=True)

    # Register the routes with the app
    app.register_blueprint(main)
    app.register_blueprint(api)

    return app