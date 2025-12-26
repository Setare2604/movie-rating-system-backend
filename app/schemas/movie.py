from pydantic import BaseModel, Field
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

class MovieCreate(BaseModel):
    title: str = Field(..., min_length=1, max_length=255)
    director_id: int
    genre_ids: List[int] = Field(default_factory=list)

class MovieCreatedOut(BaseModel):
    id: int
    title: str
    director_id: int
    genres: List[str]

    class Config:
        from_attributes = True