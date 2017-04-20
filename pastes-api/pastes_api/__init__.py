import logging

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

from pastes_api.config import Config
from pastes_api.render import respond_only_json
from pastes_api.logger import create_file_handler, log_requests, create_stream_handler


# Config App
config = Config()
app = Flask(__name__)
app.config.from_object(config)
respond_only_json(app)
marshall = Marshmallow(app)

# Config logging
log_requests(app)

logging.getLogger("werkzeug").setLevel(logging.WARNING)
app.logger.addHandler(create_stream_handler())

if not config.DEBUG:
    app.logger.addHandler(create_file_handler(config.LOG_OUTPUT_PATH))
    app.logger.setLevel(logging.INFO)

# Config DB
db = SQLAlchemy(app)
Migrate(app, db)

# Config Flask Script
manager = Manager(app)
manager.add_command('db', MigrateCommand)

# Register model
from pastes_api import model

# Register routes
from pastes_api import routes
