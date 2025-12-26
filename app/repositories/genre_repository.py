from sqlalchemy.orm import Session
from app.models.genre import Genre

def create_genre(db: Session, name: str) -> Genre:
    g = Genre(name=name)
    db.add(g)
    db.commit()
    db.refresh(g)
    return g