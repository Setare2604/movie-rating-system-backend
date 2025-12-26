from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from app.db.database import get_db
from app.schemas.movie import MovieOut
from app.repositories.movie_repository import get_movies_with_stats

router = APIRouter(prefix="/movies", tags=["movies"])

@router.get("", response_model=List[MovieOut])
def list_movies(db: Session = Depends(get_db)):
    return get_movies_with_stats(db)