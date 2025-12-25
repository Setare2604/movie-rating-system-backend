from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from sqlalchemy import text

from app.db.database import get_db

app = FastAPI(title="Movie Rating System API")

@app.get("/")
def root():
    return {"status": "success", "message": "API is running"}

@app.get("/health/db")
def db_health_check(db: Session = Depends(get_db)):
    db.execute(text("SELECT 1"))
    return {"status": "success", "message": "Database connection is OK"}