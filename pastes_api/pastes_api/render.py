from flask import make_response, jsonify
from werkzeug.exceptions import default_exceptions, HTTPException, NotFound
import json


def json_response(status:int, data):
    response = make_response()
    response.status_code = status
    response.content_type = 'application/json'
    response.data = json.dumps(data)
    return response

def json_error(status:int, message):
    return json_response(status, {"error": message})

def respond_only_json(flask_app):
    """All error responses will reply this instead"""

    def ex_to_json_error(ex):
        if isinstance(ex, HTTPException):              
            status = ex.code
            message = ex.description
        else:
            status = 500
            message = 'Something went wrong, that\'s all we know'
        return json_error(status, message)

    for key in default_exceptions:
        flask_app.error_handler_spec[None][key] = {object: ex_to_json_error}

    return flask_app