from typing import Annotated
from datetime import datetime

from pydantic import BaseModel, Field, BeforeValidator
from .validations import is_valid_obj_id

PyObjectId = Annotated[str, BeforeValidator(is_valid_obj_id)]


class MongoModel(BaseModel):
    id: PyObjectId = Field(alias='_id', default=None)


class ToDo(BaseModel):
    content: str = Field(min_length=1, max_length=96)
    open: bool = True
    creation_date: datetime = Field(default_factory=datetime.today)
    deadline_date: datetime | None = None


class UpdateToDo(BaseModel):
    content: str | None = None
    open: bool | None = None
    deadline_date: datetime | None = None


class MongoToDo(ToDo, MongoModel):
    pass


class MongoToDoList(BaseModel):
    todos: list[MongoToDo]
