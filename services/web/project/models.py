from project import db
from sqlalchemy.orm import relationship


# class Status(db.Model):
#     __tablename__ = "status"
#
#     status_id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(32), unique=True, nullable=False)
#     users = relationship("User", back_populates="status")
#
#     def __init__(self, name):
#         self.name = name


class User(db.Model):
    __tablename__ = "user"

    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(32), unique=True, nullable=False)
    email = db.Column(db.String(64), unique=True, nullable=False)
    password = db.Column(db.String(64), nullable=False)
    added_films = relationship("Film", back_populates="user")
    # status_id = db.Column(db.Integer, db.ForeignKey('status.status_id'))
    # status = relationship("Status", back_populates="users")


film_director = db.Table("film_director", db.Model.metadata,
                         db.Column("film_id", db.Integer, db.ForeignKey("film.id")),
                         db.Column("director_id", db.Integer, db.ForeignKey("director.id")))


class Director(db.Model):
    __tablename__ = "director"

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(32), nullable=False)
    last_name = db.Column(db.String(32), nullable=False)
    birth_date = db.Column(db.Date)
    films = relationship("Film", secondary=film_director, back_populates="directors")

    def __repr__(self):
        return self.first_name + " " + self.last_name


film_genre = db.Table("film_genre", db.Model.metadata,
                      db.Column('id', db.Integer, primary_key=True),
                      db.Column("film_id", db.Integer, db.ForeignKey("film.id")),
                      db.Column("genre_id", db.Integer, db.ForeignKey("genre.id")))


class Genre(db.Model):
    __tablename__ = "genre"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), nullable=False)
    films = relationship("Film", secondary=film_genre, back_populates="genres")

    def __repr__(self):
        return self.name


class Film(db.Model):
    __tablename__ = "film"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64), nullable=False)
    release_date = db.Column(db.Date, nullable=False)
    description = db.Column(db.Text)
    rating = db.Column(db.Numeric, nullable=False)
    poster = db.Column(db.Text)
    user_id = db.Column(db.Integer, db.ForeignKey("user.user_id"))
    user = relationship("User", back_populates="added_films")
    directors = relationship("Director", secondary=film_director, back_populates="films")
    genres = relationship("Genre", secondary=film_genre, back_populates="films")
