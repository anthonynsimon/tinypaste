import time

from marshmallow import post_load, fields

from pastes_api import db, marshall


class Paste(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.Integer)
    content = db.Column(db.String(2048))

    def __init__(self, content, created_at=None):
        self.created_at = created_at if created_at is not None else int(
            time.time())
        self.content = content


class PasteSchema(marshall.ModelSchema):
    class Meta:
        model = Paste

    id = fields.Int()
    content = fields.String()
    created_at = fields.DateTime()

    @post_load
    def make_paste(self, data):
        print(data)
        return Paste(**data)


paste_schema = PasteSchema()
