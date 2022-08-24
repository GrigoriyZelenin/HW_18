from dao.model.director import Director
from dao.model.genre import Genre
from setup_db import db

class Movie(db.Model):
    __tablename__ = 'movie'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    description = db.Column(db.String)
    trailer = db.Column(db.String)
    year = db.Column(db.Integer)
    rating = db.Column(db.Float)
    genre_id = db.Column(db.Integer, db.ForeignKey(f'{Genre.__tablename__}.id'))
    director_id = db.Column(db.Integer, db.ForeignKey(f'{Director.__tablename__}.id'))
    genre = db.relationship('Genre')
    director = db.relationship('Director')