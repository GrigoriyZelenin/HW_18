from marshmallow import Schema, fields


class DirectorSchema(Schema):
    id = fields.Integer()
    name = fields.Str()
