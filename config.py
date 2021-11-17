""" Flask Configuration. """

from os import environ, path
#from dotenv import load_dotenv


basedir = path.abspath(path.dirname(__file__))
# set environment variables in a local file called .env instead and grab those variables using a Python library like python-dotenv
#load_dotenv(path.join(basedir,'.env'))

class Config:
    """ 
    Base config. 
    To make configuration more flexible and safe, most settings can be optionally impor‐ ted 
    from environment variables. For example, the value of the SECRET_KEY, due to its sensitive nature, 
    can be set in the environment, but a default value is provided in case the environment does not define it.
    
    """
    SECRET_KEY = environ.get('SECRET_KEY') or 'pass123$'
    #SESSION_COOKIE_NAME = environ.get('SESSION_COOKIE_NAME') error cookie
    #BOOTSTRAP_SERVE_LOCAL = True
    STATIC_FOLDER = 'static'
    TEMPLATES_FOLDER = 'templates'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    @staticmethod
    def init_app(app):
        pass


class ProdConfig(Config):
    FLASK_ENV = 'production'
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = environ.get('DEV_DATABASE_URL') or \
    'sqlite:///' + path.join(basedir, 'data-prod.sqlite')

class DevConfig(Config):
    FLASK_ENV = 'development'
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = environ.get('DEV_DATABASE_URL') or \
    'sqlite:///' + path.join(basedir, 'data-dev.sqlite')


class TestConfig(Config):
    FLASK_ENV = 'testing'
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = environ.get('DEV_DATABASE_URL') or \
    'sqlite://'


