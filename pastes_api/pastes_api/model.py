import datetime

from marshmallow import post_load, fields

from pastes_api import db, marshall


class Paste(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.String(32), nullable=True)
    content = db.Column(db.String(2048), nullable=False)

    def __init__(self, content, created_at=None):
        self.content = content
        if created_at is not None:
            self.created_at = created_at
        else:
            self.created_at = datetime.datetime.now().isoformat()


class PasteSchema(marshall.ModelSchema):
    class Meta:
        model = Paste


paste_schema = PasteSchema()
