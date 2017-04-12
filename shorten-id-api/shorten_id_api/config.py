from dotenv import load_dotenv, find_dotenv

import os


class Config(object):
    """
    Configuration file for Flask App
    Use dotenv (.env) file to override the default values.
    """

    load_dotenv(find_dotenv())
