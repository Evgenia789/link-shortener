import os
from app.database.db import db

from flask import Flask

def create_app(name_config="config.DevelopmentConfig"):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(name_config)

    db.init_app(app)
    with app.test_request_context():
        db.create_all()

    return app
