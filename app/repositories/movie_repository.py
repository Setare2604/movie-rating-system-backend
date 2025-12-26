from sqlalchemy.orm import Session
from sqlalchemy import func
from fastapi import HTTPException
from app.models.movie import Movie
from app.models.director import Director
from app.models.genre import Genre
from app.models.movie_rating import MovieRating

def get_movies_with_stats(db: Session):
    # Aggregations: avg + count
    avg_rating = func.avg(MovieRating.rating).label("average_rating")
    ratings_count = func.count(MovieRating.id).label("ratings_count")

    rows = (
        db.query(
            Movie.id,
            Movie.title,
            Director.name.label("director_name"),
            avg_rating,
            ratings_count,
        )
        .join(Director, Movie.director_id == Director.id)
        .outerjoin(MovieRating, MovieRating.movie_id == Movie.id)
        .group_by(Movie.id, Director.name)
        .all()
    )

    # Genres for each movie (separate query to keep it simple & reliable)
    result = []
    for r in rows:
        genre_names = (
            db.query(Genre.name)
            .join(Genre.movies)
            .filter(Movie.id == r.id)
            .all()
        )
        result.append(
            {
                "id": r.id,
                "title": r.title,
                "director_name": r.director_name,
                "genres": [g[0] for g in genre_names],
                "average_rating": float(r.average_rating) if r.average_rating is not None else None,
                "ratings_count": int(r.ratings_count),
            }
        )

    return result

def create_movie(db: Session, title: str, director_id: int, genre_ids: list[int]) -> Movie:
    director = db.query(Director).filter(Director.id == director_id).first()
    if not director:
        raise HTTPException(status_code=404, detail="Director not found")

    genres = []
    if genre_ids:
        genres = db.query(Genre).filter(Genre.id.in_(genre_ids)).all()
        if len(genres) != len(set(genre_ids)):
            raise HTTPException(status_code=404, detail="One or more genres not found")

    movie = Movie(title=title, director_id=director_id)
    movie.genres = genres

    db.add(movie)
    db.commit()
    db.refresh(movie)
    return movie