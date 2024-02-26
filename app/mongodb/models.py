from pydantic import BaseModel, Field


class ToDo(BaseModel):
    content: str = Field(min_length=1, max_length=128)
    open: bool
