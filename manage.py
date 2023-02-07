from app.database.db import db
from app.short_link.models import Link
from flask import Flask, app
from flask_bootstrap import Bootstrap


def get_flask_app(config: str = "config.DevelopmentConfig") -> app.Flask:
    """
    Initializes Flask app with given configuration.
    Main entry point for wsgi (gunicorn) server.
    :param config: Configuration dictionary
    :return: app
    """
    app = Flask(__name__, instance_relative_config=True,
                template_folder='app/templates')
    app.config.from_object(config)

    db.init_app(app)
    with app.app_context():
        db.create_all()
    
    from app.short_link import views
    
    app.register_blueprint(views.module)
    bootstrap = Bootstrap(app)

    return app


if __name__ == '__main__':
    app = get_flask_app()
    app.run()
