import json

from flask import request
from marshmallow import ValidationError

from pastes_api import app, db
from pastes_api.model import Paste, paste_schema
from pastes_api.render import json_response, json_error
from pastes_api.errors import not_found_error, validation_error


@app.route("/pastes/<id>", methods=['GET'])
def get_paste(id):
    paste = db.session.query(Paste).get(id)
    result = paste_schema.dump(paste).data
    app.logger.debug(result)
    if result is None or not result:
        return json_error(404, not_found_error("No paste with such id found."))
    return json_response(200, result)


@app.route("/pastes", methods=['POST'])
def create_paste():
    try:
        paste = paste_schema.load(json.loads(request.data)).data
    except ValidationError as err:
        return json_error(400, validation_error(err.messages))
    db.session.add(paste)
    db.session.commit()
    result = paste_schema.dump(paste).data
    return json_response(201, result)
