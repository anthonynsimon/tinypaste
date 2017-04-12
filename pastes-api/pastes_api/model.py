import datetime

from marshmallow import post_dump, fields, ValidationError, validates

from pastes_api import db, marshall


class Paste(db.Model):
    __tablename__ = 'pastes'

    id = db.Column(
        db.Integer,
        primary_key=True)

    created_at = db.Column(
        db.String(32),
        nullable=False,
        default=datetime.datetime.utcnow)

    content = db.Column(
        db.String(2048),
        nullable=False)


class PasteSchema(marshall.ModelSchema):
    class Meta:
        model = Paste

    @post_dump
    def process_dump(self, data):
        data.pop('id')
        return data

    @validates('content')
    def validate_content(self, value):
        if len(value) > 2048:
            raise ValidationError()


paste_schema = PasteSchema(strict=True)
