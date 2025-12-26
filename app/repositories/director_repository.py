from sqlalchemy.orm import Session
from app.models.director import Director

def create_director(db: Session, name: str) -> Director:
    d = Director(name=name)
    db.add(d)
    db.commit()
    db.refresh(d)
    return d