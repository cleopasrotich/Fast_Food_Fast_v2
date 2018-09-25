from flask import Flask,app
from instance.config import app_config


def create_app(config_name):

    app = Flask(__name__)
    return app
