from dotenv import load_dotenv, find_dotenv

import os


class Config(object):
    """
    Configuration file for Flask App
    Use dotenv (.env) file to override the default values.
    """

    load_dotenv(find_dotenv())

    APP_HOST = os.environ.get('APP_HOST', '127.0.0.1')
    APP_PORT = int(os.environ.get('APP_PORT', 5000))
    DEBUG = os.environ.get('DEBUG', False)

    SHORTEN_ID_SERVICE_ADDRESS = os.environ.get('SHORTEN_ID_SERVICE_ADDRESS')

    DATABASE = os.environ.get('DATABASE')
    SECRET_KEY = os.environ.get('SECRET_KEY', 'secret')
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = os.environ.get('SQLALCHEMY_TRACK_MODIFICATIONS', False)
