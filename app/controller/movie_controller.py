from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from app.db.database import get_db
from app.schemas.movie import MovieOut, MovieCreate, MovieCreatedOut
from app.repositories.movie_repository import get_movies_with_stats, create_movie

router = APIRouter(prefix="/movies", tags=["movies"])

@router.get("", response_model=List[MovieOut])
def list_movies(db: Session = Depends(get_db)):
    return get_movies_with_stats(db)

@router.post("", response_model=MovieCreatedOut)
def add_movie(payload: MovieCreate, db: Session = Depends(get_db)):
    movie = create_movie(
        db,
        title=payload.title,
        director_id=payload.director_id,
        genre_ids=payload.genre_ids,
    )
    return {
        "id": movie.id,
        "title": movie.title,
        "director_id": movie.director_id,
        "genres": [g.name for g in movie.genres],
    }