from dao.model.director_schema import DirectorSchema
from dao.model.genre_schema import GenreSchema
from marshmallow import Schema, fields


class MovieSchema(Schema):
    id = fields.Int()
    title = fields.Str()
    description = fields.Str()
    trailer = fields.Str()
    year = fields.Int()
    rating = fields.Float()
    genre_id = fields.Int()
    director_id = fields.Int()
    genre = fields.Nested(GenreSchema)
    director = fields.Nested(DirectorSchema)
