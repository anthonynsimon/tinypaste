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
    LOG_OUTPUT_PATH = os.environ.get('LOG_OUTPUT_PATH', '/var/log/app.log')
