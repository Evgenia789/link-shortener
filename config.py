import os


class Config(object):
    DEBUG = False
    # Включение защиты против "Cross-site Request Forgery (CSRF)"
    CSRF_ENABLED = True
    SECRET_KEY = os.environ['SECRET_KEY']
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(Config):
    FLASK_ENV = 'production'
    DEBUG = False


class DevelopmentConfig(Config):
    FLASK_ENV = 'development'
    DEVELOPMENT = True
    DEBUG = True
