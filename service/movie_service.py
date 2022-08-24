from dao.model.movie import Movie
from dao.movie_dao import MovieDAO


class MovieService:

    def __init__(self, movie_dao: MovieDAO):
        self.movie_dao = movie_dao

    def get_movies(self) -> list[Movie]:
        return self.movie_dao.get_all_movie()

    def get_movie_by_request(self, **kwargs) -> list[Movie]:
        return self.movie_dao.get_movie_by_many_param(**kwargs)

    def add_movie(self, data) -> None:
        self.movie_dao.create(**data)

    def update_movie(self, data:dict) -> None:
        self.movie_dao.update(data)

    def delete_movie_by_id(self, id: int) -> None:
        self.movie_dao.delete(id)
