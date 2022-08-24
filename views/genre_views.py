from flask_restx import Resource, Namespace

from dao.model.genre_schema import GenreSchema
from implemented import genre_service

genre_ns = Namespace('genres')
genre_schema = GenreSchema()
genres_schema = GenreSchema(many=True)


@genre_ns.route('/')
class GenresView(Resource):
    def get(self):
        return genres_schema.dump(genre_service.get_genres()), 200


@genre_ns.route('/<int:gid>')
class GenresView(Resource):
    def get(self, gid: int):
        return genre_schema.dump(genre_service.get_genre_by_id(gid)), 200
