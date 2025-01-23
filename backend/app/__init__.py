from flask import Flask
from .routes import api, main

def create_app():

    app = Flask(__name__)
    app.register_blueprint(main)
    app.register_blueprint(api)

    return app