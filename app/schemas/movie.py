from pydantic import BaseModel
from typing import List, Optional

class MovieOut(BaseModel):
    id: int
    title: str
    director_name: str
    genres: List[str]
    average_rating: Optional[float] = None
    ratings_count: int

    class Config:
        from_attributes = True