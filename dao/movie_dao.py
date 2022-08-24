from dao.model.movie import Movie


class MovieDAO:
    def __init__(self, session):
        self.session = session

    def get_all_movie(self):
        return self.session.query(Movie).all()

    def get_movie_by_id(self, id: int):
        return self.session.query(Movie).filter(Movie.id == id).one()

    def get_movie_by_directir(self, director_id: int):
        return self.session.query(Movie).filter(Movie.director_id == director_id).all()

    def get_movie_by_genre(self, genre_id: int):
        return self.session.query(Movie).filter(Movie.genre_id == genre_id).all()

    def get_movie_by_year(self, year: int):
        return self.session.query(Movie).filter(Movie.year == year).all()

    def get_movie_by_many_param(self, **kwargs):

        return self.session.query(Movie).filter_by(
            **{k: v for k, v in kwargs.items() if v is not None}
        ).all()

    def create(self, **kwargs):
        try:
            self.session.add(
                Movie(**kwargs))
            self.session.commit()
            return 'Успешно добавлено'

        except Exception as e:
            self.session.rollback()
            return e

    def update(self, kwargs:dict):
        try:
            self.session.query(Movie).filter(Movie.id == kwargs.get('id')).update(kwargs)
            self.session.commit()
            return 'Успешно обновлено'
        except Exception as e:
            self.session.rollback()
            return e

    def delete(self, id: int):
        try:
            self.session.query(Movie).filter(Movie.id == id).delete()
            self.session.commit()
            return 'Успешно удалено'
        except Exception as e:
            self.session.rollback()
            return e
