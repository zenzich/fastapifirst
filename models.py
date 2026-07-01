from pydantic import BaseModel, Field

class Book(BaseModel):
    title: str = Field(min_length=1, max_length=50)
    text: str = Field(min_length=1, max_length=10000)