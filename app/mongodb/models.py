from typing import Annotated

from pydantic import BaseModel, Field, BeforeValidator
from .validations import is_valid_obj_id

PyObjectId = Annotated[str, BeforeValidator(is_valid_obj_id)]


class MongoModel(BaseModel):
    id: PyObjectId = Field(alias='_id', default=None)


class ToDo(BaseModel):
    content: str = Field(min_length=1, max_length=96)
    open: bool = True


class UpdateToDo(BaseModel):
    content: str | None = None
    open: bool | None = None


class MongoToDo(ToDo, MongoModel):
    pass


class MongoToDoList(BaseModel):
    todos: list[MongoToDo]
