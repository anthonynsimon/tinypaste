from dotenv import load_dotenv, find_dotenv

import os


class Config(object):
    """
    Configuration file for Flask App
    Use dotenv (.env) file to override the default values.
    """

    load_dotenv(find_dotenv())

    DATABASE = os.environ.get('DATABASE')
    SECRET_KEY = os.environ.get('SECRET_KEY', 'secret')
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = os.environ.get(
        'SQLALCHEMY_TRACK_MODIFICATIONS', False)

    MYSQL_HOST = os.environ.get('MYSQL_HOST')
    MYSQL_USER = os.environ.get('MYSQL_USER')
    MYSQL_PASSWORD = os.environ.get('MYSQL_PASSWORD')
    MYSQL_DB = os.environ.get('MYSQL_DB')
    MYSQL_PORT = os.environ.get('MYSQL_PORT')
