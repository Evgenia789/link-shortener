import os
from app.database.db import db
from app.short_link.models import Link
from flask import Flask
from flask_bootstrap import Bootstrap

def create_app(name_config="config.DevelopmentConfig"):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True, template_folder='app/templates')
    app.config.from_object(name_config)
    # app.config.from_envvar('YOURAPPLICATION_SETTINGS')

    db.init_app(app)
    with app.app_context():
        db.create_all()
    
    from app.short_link import views
    
    app.register_blueprint(views.module)
    bootstrap = Bootstrap(app)

    return app


if __name__ == '__main__':
    create_app().run()