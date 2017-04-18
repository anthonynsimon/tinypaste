from flask import Flask

from shorten_id_api.config import Config
from shorten_id_api.render import respond_only_json

# Config App
config = Config()
app = Flask(__name__)
app.config.from_object(config)
respond_only_json(app)

# Register routes
from shorten_id_api import routes
