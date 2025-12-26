from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.schemas.genre import GenreCreate, GenreOut
from app.repositories.genre_repository import create_genre

router = APIRouter(prefix="/genres", tags=["genres"])

@router.post("", response_model=GenreOut)
def add_genre(payload: GenreCreate, db: Session = Depends(get_db)):
    return create_genre(db, payload.name)