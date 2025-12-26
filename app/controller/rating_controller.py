from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.schemas.rating import RatingCreate
from app.repositories.rating_repository import add_rating
from app.models.movie import Movie

router = APIRouter(prefix="/movies", tags=["ratings"])

@router.post("/{movie_id}/ratings")
def create_rating(movie_id: int, payload: RatingCreate, db: Session = Depends(get_db)):
    movie = db.query(Movie).filter(Movie.id == movie_id).first()
    if not movie:
        raise HTTPException(status_code=404, detail="Movie not found")

    r = add_rating(db, movie_id=movie_id, rating=payload.rating)
    return {"status": "success", "rating_id": r.id, "movie_id": movie_id, "rating": r.rating}