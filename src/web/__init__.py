from flask import Flask
from .views import *


def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "f8ejf85g4jf03i48jf389jfj39"
    app.register_blueprint(views, url_prefix="/")
    return app
