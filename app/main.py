from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from sqlalchemy import text

from app.db.database import get_db

from app.controller.movie_controller import router as movie_router
from app.controller.rating_controller import router as rating_router

app = FastAPI(title="Movie Rating System API")

app.include_router(movie_router)
app.include_router(rating_router)


@app.get("/")
def root():
    return {"status": "success", "message": "API is running"}

@app.get("/health/db")
def db_health_check(db: Session = Depends(get_db)):
    db.execute(text("SELECT 1"))
    return {"status": "success", "message": "Database connection is OK"}