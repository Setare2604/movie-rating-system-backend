from sqlalchemy import Table, Column, ForeignKey
from sqlalchemy import Integer
from app.db.database import Base

genres_movie = Table(
    "genres_movie",
    Base.metadata,
    Column("movie_id", Integer, ForeignKey("movies.id"), primary_key=True),
    Column("genre_id", Integer, ForeignKey("genres.id"), primary_key=True),
)