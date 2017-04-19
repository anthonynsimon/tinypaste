import json

from flask import request
from marshmallow import ValidationError
import requests 
import json

from pastes_api import app, db, config
from pastes_api.model import Paste, paste_schema
from pastes_api.render import json_response, json_error
from pastes_api.errors import not_found_error, validation_error, internal_error
from pastes_api.cache import cache

@app.route("/pastes/<short_id>", methods=['GET'])
def get_paste(short_id):
    cache_key = add_cache_key_prefix(short_id)
    from_cache = cache.get(cache_key)
    if from_cache is None:
        try:
            id = unshorten_id(short_id)
        except Exception as ex:
            app.logger.debug(ex)
            return json_error(500, internal_error())

        paste = db.session.query(Paste).get(id)
        result = paste_schema.dump(paste).data
        if result is None or not result:
            return json_error(404, not_found_error("No paste with such id found."))

        cache.set(cache_key, json.dumps(result))
        app.logger.debug("Retrieved paste with short id: {} from database".format(short_id))
    else:
        paste = paste_schema.load(json.loads(from_cache.decode('utf-8'))).data
        result = paste_schema.dump(paste).data
        app.logger.debug("Retrieved paste with short id: {} from cache".format(short_id))

    return json_response(200, result)


@app.route("/pastes", methods=['POST'])
def create_paste():
    try:
        paste = paste_schema.load(request.get_json()).data
    except ValidationError as err:
        return json_error(400, validation_error(err.messages))
    db.session.add(paste)
    db.session.commit()

    try:
        short_id = shorten_id(paste.id)
    except:
        app.logger.debug(err.message)
        return json_error(500, internal_error())
        
    result = paste_schema.dump(paste).data
    result['short_id'] = short_id
    return json_response(201, result)

def shorten_id(id):
    url = "{0}/shorten?id={1}".format(config.SHORTEN_ID_SERVICE_ADDRESS, id)
    r = requests.post(url)
    if r.status_code != requests.codes.ok:
        raise Exception("Couldn't connect with shorten id service")

    short_id = r.json().get('short_id')
    if short_id is None:
        raise Exception("Shorten id service replied with null short_id")
    
    return short_id

def unshorten_id(short_id):
    url = "{0}/unshorten?short_id={1}".format(config.SHORTEN_ID_SERVICE_ADDRESS, short_id)
    r = requests.post(url)
    if r.status_code != requests.codes.ok:
        raise Exception("Couldn't connect with shorten id service")

    id = r.json().get('id')
    if id is None:
        raise Exception("Shorten id service replied with null id")
    
    return id

def add_cache_key_prefix(key):
    return "tinypaste:short_id:{}".format(key)