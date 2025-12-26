from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from sqlalchemy import text

from app.db.database import get_db

from app.controller.movie_controller import router as movie_router
from app.controller.rating_controller import router as rating_router
from app.controller.director_controller import router as director_router
from app.controller.genre_controller import router as genre_router

app = FastAPI(title="Movie Rating System API")

API_PREFIX = "/api/v1"
app.include_router(movie_router, prefix=API_PREFIX)
app.include_router(rating_router, prefix=API_PREFIX)
app.include_router(director_router, prefix=API_PREFIX)
app.include_router(genre_router, prefix=API_PREFIX)

@app.get("/")
def root():
    return {"status": "success", "message": "API is running"}

@app.get("/health/db")
def db_health_check(db: Session = Depends(get_db)):
    db.execute(text("SELECT 1"))
    return {"status": "success", "message": "Database connection is OK"}