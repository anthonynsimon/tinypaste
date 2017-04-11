import json

from flask import request

from pastes_api import app, db
from pastes_api.model import Paste, paste_schema
from pastes_api.render import json_response


@app.route("/pastes/<id>", methods=['GET'])
def index(id):
    return id


@app.route("/pastes", methods=['POST'])
def create_paste():
    paste = paste_schema.load(json.loads(request.data)).data
    # result = paste_schema.dump(paste).data
    return json_response(201, paste)
    db.session.add(paste)
    db.session.commit()
    return paste
