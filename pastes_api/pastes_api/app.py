"""
	Pastes API
	--------------------
	The microservice for creating and retrieving pastes.

	:copyright: (c) Anthony Najjar Simon 2017
	:license: MIT, see LICENSE for more details
"""

from flask import Flask

from .render import respond_only_json

# Init App
app = Flask(__name__)
app.config.from_envvar('PASTES_API_CONFIG', silent=False)
respond_only_json(app)
