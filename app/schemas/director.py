from pydantic import BaseModel, Field

class DirectorCreate(BaseModel):
    name: str = Field(..., min_length=1, max_length=255)

class DirectorOut(BaseModel):
    id: int
    name: str

    class Config:
        from_attributes = True