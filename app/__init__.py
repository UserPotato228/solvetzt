import os

# imports
from flask import Flask, request, send_from_directory
from config import Config
from app.extensions import db


# create app func
def create_app(config_class=Config):
    # start flask
    app = Flask(__name__)
    app.config.from_object(config_class)

    # init db
    db.init_app(app)

    from app.index import bp as index_bp
    app.register_blueprint(index_bp)
    from app.tasks import bp as tasks_bp
    app.register_blueprint(tasks_bp)

    # return app
    return app
