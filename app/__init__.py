from flask import Flask
from flask_bootstrap import Bootstrap

bootstrap = Bootstrap()

def create_app():

    app = Flask(__name__)

    bootstrap = Bootstrap()

    return app