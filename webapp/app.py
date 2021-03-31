from flask import Flask
from flask_cors import CORS

def create_app(config_object):
    app = Flask(__name__)
    CORS(app)
    app.config.from_object(config_object)
    with app.app_context():
        return app