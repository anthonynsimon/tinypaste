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
    DEBUG = os.environ.get('DEBUG', "False").lower() in ("yes", "true", "t", "1")

    LOG_OUTPUT_PATH = os.environ.get('LOG_OUTPUT_PATH', '/var/log/app.log')

    SHORTEN_ID_SERVICE_ADDRESS = os.environ.get('SHORTEN_ID_SERVICE_ADDRESS')

    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = os.environ.get('SQLALCHEMY_TRACK_MODIFICATIONS', False)

    REDIS_HOST = os.environ.get('REDIS_HOST')
    REDIS_PORT = os.environ.get('REDIS_PORT')
    REDIS_DB = os.environ.get('REDIS_DB')