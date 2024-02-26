from typing import Annotated

from pydantic import BaseModel, Field, BeforeValidator

py_object_id = Annotated[str, BeforeValidator(str)]


class MongoModel(BaseModel):
    id: py_object_id = Field(alias='_id', default=None)


class ToDo(BaseModel):
    content: str = Field(min_length=1, max_length=96)
    open: bool


class UpdateToDo(BaseModel):
    content: str | None = None
    open: bool | None = None


class MongoToDo(ToDo, MongoModel):
    pass
