from schema import Schema, And, Use

import json

paste_schema = Schema(And(Use(json.loads), {
    'short_link': str,
    'created_at': int,
    'content': str
}))

create_paste_schema = Schema(And(Use(json.loads), {
    'content': str
}))
