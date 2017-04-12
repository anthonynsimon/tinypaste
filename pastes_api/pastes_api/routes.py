import json

from flask import request

from pastes_api import app, db
from pastes_api.model import Paste, paste_schema
from pastes_api.render import json_response, json_error


@app.route("/pastes/<id>", methods=['GET'])
def index(id):
    paste = db.session.query(Paste).get(id)
    result = paste_schema.dump(paste).data
    app.logger.debug(result)
    if result is None or not result:
        return json_error(404, "no paste with such id found")
    return json_response(200, result)


@app.route("/pastes", methods=['POST'])
def create_paste():
    paste = paste_schema.load(json.loads(request.data)).data
    db.session.add(paste)
    db.session.commit()
    result = paste_schema.dump(paste).data
    return json_response(201, result)
