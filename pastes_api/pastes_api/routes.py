from flask import request
from werkzeug.exceptions import BadRequest, NotFound, InternalServerError
import time

from .app import app
from .store import database
from .paste import paste_schema, create_paste_schema
from .render import json_response


@app.route('/pastes/<string:id>', methods=['GET'])
def get_paste(id):
    """Retrieves a paste by ID"""

    try:
        cursor = database.connection.cursor()
        cursor.execute(
            """SELECT id, content, created_at FROM pastes WHERE id = %s;""", id)
    except:
        raise NotFound

    row = cursor.fetchone()
    if row is None:
        raise InternalServerError

    paste = row_to_paste(row)

    return json_response(200, paste)


@app.route('/pastes', methods=['POST'])
def create_paste():
    """Creates a paste and returns its ID"""

    # TODO: make this nicer!
    try:
        payload = create_paste_schema.validate(request.data)
    except:
        raise BadRequest()

    try:
        conn = database.connection
        try:
            cursor = conn.cursor()
            cursor.execute("""INSERT INTO pastes (content, created_at) VALUES (%s, %s);""",
                           (payload['content'], int(time.time())))
            cursor.execute(
                """SELECT id, content, created_at FROM pastes WHERE id = last_insert_id();""")
            conn.commit()
        except:
            conn.rollback()
            raise InternalServerError
    except:
        raise InternalServerError

    row = cursor.fetchone()
    if row is None:
        raise InternalServerError

    paste = row_to_paste(row)

    return json_response(201, paste)


def row_to_paste(row):
    paste = {}
    paste['id'] = row[0]
    paste['content'] = row[1]
    paste['created_at'] = row[2]
    return paste
