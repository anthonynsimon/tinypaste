import json

from flask import request

from shorten_id_api import app
from shorten_id_api.render import json_response, json_error
from shorten_id_api.errors import validation_error
from shorten_id_api.shortener import encode_id, decode_id


@app.route("/shorten", methods=["POST"])
def shorten():
    id = request.args.get("id")
    casted, valid = validate_id(id)
    if not valid:
        return json_error(400, validation_error({"id": ["Not a valid numeric value or missing."]}))
    short_id = encode_id(casted)
    return json_response(200, {"short_id": short_id})


@app.route("/unshorten", methods=["POST"])
def unshorten():
    short_id = request.args.get("short_id")
    if not is_short_id_valid(short_id):
        return json_error(400, validation_error({"short_id": ["Invalid or missing value"]}))
    id = decode_id(short_id)
    return json_response(200, id)


def validate_id(id):
    valid = False
    casted = -1
    try:
        casted = int(id)
    except ValueError:
        valid = False

    if casted >= 0:
        valid = True

    return casted, valid


def is_short_id_valid(short_id):
    return short_id is not None and len(short_id) > 0
