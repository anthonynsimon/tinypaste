import logging

from flask import Flask
from flask_script import Manager

from shorten_id_api.config import Config
from shorten_id_api.render import respond_only_json
from shorten_id_api.logger import create_file_handler, log_requests, create_stream_handler

# Config App
config = Config()
app = Flask(__name__)
app.config.from_object(config)
respond_only_json(app)

# Config logging
log_requests(app)

logging.getLogger("werkzeug").setLevel(logging.WARNING)
app.logger.addHandler(create_stream_handler())

if not config.DEBUG:
    app.logger.addHandler(create_file_handler(config.LOG_OUTPUT_PATH))
    app.logger.setLevel(logging.INFO)

# Config Flask Script
manager = Manager(app)

# Register routes
from shorten_id_api import routes
