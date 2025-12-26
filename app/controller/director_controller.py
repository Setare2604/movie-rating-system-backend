from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.schemas.director import DirectorCreate, DirectorOut
from app.repositories.director_repository import create_director

router = APIRouter(prefix="/directors", tags=["directors"])

@router.post("", response_model=DirectorOut)
def add_director(payload: DirectorCreate, db: Session = Depends(get_db)):
    return create_director(db, payload.name)