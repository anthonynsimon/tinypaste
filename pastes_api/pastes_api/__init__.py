import time

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

from pastes_api.config import Config
from pastes_api.render import respond_only_json


app = Flask(__name__)
app.config.from_object(Config)
respond_only_json(app)
db = SQLAlchemy(app)
marshall = Marshmallow(app)

from pastes_api import model

db.create_all()

# Register routes
from pastes_api import routes
