import os


class Config:
    """A class used to represent base config"""
    DEBUG = False
    CSRF_ENABLED = True
    SECRET_KEY = os.getenv('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    BASE_URL = os.getenv('BASE_URL')


class ProductionConfig(Config):
    """A class used to represent production config"""
    FLASK_ENV = 'production'
    DEBUG = False


class DevelopmentConfig(Config):
    """A class used to represent development config"""
    FLASK_ENV = 'development'
    DEVELOPMENT = True
    DEBUG = True
