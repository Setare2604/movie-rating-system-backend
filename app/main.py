from fastapi import FastAPI

app = FastAPI(title="Movie Rating System API")

@app.get("/")
def root():
    return {"status": "success", "message": "API is running"}