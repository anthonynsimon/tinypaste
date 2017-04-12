from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate

from pastes_api.config import Config
from pastes_api.render import respond_only_json


# Config App
app = Flask(__name__)
app.config.from_object(Config)
respond_only_json(app)
marshall = Marshmallow(app)

# Config DB
db = SQLAlchemy(app)
Migrate(app, db)

# Register model
from pastes_api import model

# Register routes
from pastes_api import routes
