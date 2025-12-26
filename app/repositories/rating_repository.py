from sqlalchemy.orm import Session
from app.models.movie_rating import MovieRating

def add_rating(db: Session, movie_id: int, rating: float) -> MovieRating:
    new_rating = MovieRating(movie_id=movie_id, rating=rating)
    db.add(new_rating)
    db.commit()
    db.refresh(new_rating)
    return new_rating