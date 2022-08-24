from flask import request
from flask_restx import Resource, Namespace

from dao.model.movie_schema import MovieSchema
from implemented import movie_service

movie_ns = Namespace('movies')

movie_schema = MovieSchema()
movies_schema = MovieSchema(many=True)


@movie_ns.route('/')
class MoviesView(Resource):
    def get(self):

        if len(request.args) > 0:
            return movies_schema.dump(movie_service.get_movie_by_request(
                **request.args))

        else:
            return movies_schema.dump(movie_service.get_movies()), 200

    def post(self):
        if movie_service.add_movie(request.json):
            return 'Успешно добавлено', 201
        else:
            return '', 503


@movie_ns.route('/<int:mid>')
class MoviesView(Resource):
    def get(self, mid: int):
        return movie_schema.dump(movie_service.get_movie_by_request(mid)), 200

    def put(self):
        movie_service.update_movie(request.json)
        return "Успешно обновлено", 201

    def delete(self, mid: int):
        movie_service.delete_movie_by_id(mid)
        return "Успешно удалено", 204
