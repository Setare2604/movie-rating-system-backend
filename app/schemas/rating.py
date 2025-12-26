from pydantic import BaseModel, Field

class RatingCreate(BaseModel):
    rating: float = Field(..., ge=0, le=10)