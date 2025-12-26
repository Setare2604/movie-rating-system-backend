import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[1]))

from sqlalchemy.orm import Session
from app.db.database import SessionLocal
from app.models.director import Director
from app.models.genre import Genre
from app.models.movie import Movie
from app.models.movie_rating import MovieRating


def seed(db: Session):
    # Genres
    action = Genre(name="Action")
    drama = Genre(name="Drama")
    comedy = Genre(name="Comedy")

    db.add_all([action, drama, comedy])
    db.commit()

    # Directors
    nolan = Director(name="Christopher Nolan")
    fincher = Director(name="David Fincher")

    db.add_all([nolan, fincher])
    db.commit()

    # Movies
    m1 = Movie(title="Inception", director_id=nolan.id)
    m1.genres = [action, drama]

    m2 = Movie(title="Fight Club", director_id=fincher.id)
    m2.genres = [drama]

    db.add_all([m1, m2])
    db.commit()

    # Ratings
    db.add_all([
        MovieRating(movie_id=m1.id, rating=9.0),
        MovieRating(movie_id=m1.id, rating=8.5),
        MovieRating(movie_id=m2.id, rating=8.8),
    ])
    db.commit()


def main():
    db = SessionLocal()
    try:
        seed(db)
        print("✅ Seed completed successfully")
    finally:
        db.close()


if __name__ == "__main__":
    main()