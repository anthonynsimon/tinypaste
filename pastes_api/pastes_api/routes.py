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

    cur = database.connection.cursor()
    try:
        cur.execute(
            """SELECT id, content, created_at FROM pastes WHERE id = %s;""", id)
    except:
        raise NotFound

    rows = cur.fetchall()
    if len(rows) is 0:
        raise NotFound

    paste = {}
    paste['id'] = rows[0][0]
    paste['content'] = rows[0][1]
    paste['created_at'] = rows[0][2]

    return json_response(200, paste)


@app.route('/pastes', methods=['POST'])
def create_paste():
    """Creates a paste and returns its ID"""

    try:
        payload = create_paste_schema.validate(request.data)
    except:
        raise BadRequest()

    conn = database.connection
    cursor = conn.cursor()
    try:
        cursor.execute("""INSERT INTO pastes (content, created_at) VALUES (%s, %s);""",
                       (payload['content'], int(time.time())))
        cursor.execute(
            """SELECT id, content, created_at FROM pastes WHERE id = last_insert_id();""")
        conn.commit()
    except:
        conn.rollback()
        raise InternalServerError

    rows = cursor.fetchone()
    if rows is None:
        raise InternalServerError

    paste = {}
    paste['id'] = rows[0]
    paste['content'] = rows[1]
    paste['created_at'] = rows[2]

    return json_response(201, paste)
