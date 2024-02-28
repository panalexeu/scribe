from langchain.pydantic_v1 import BaseModel, Field
from langchain.tools import tool

from .prompt_template import (
    DESCRIPTION_FIELD,
    CONTENT_FIELD,
    OPEN_FIELD,
    DEADLINE_FIELD
)
from ..mongodb import ToDoRepository, ToDo


class ToolInput(BaseModel):
    collection_name: str = Field(description=DESCRIPTION_FIELD)


class ToDoInput(ToolInput):
    content: str = Field(description=CONTENT_FIELD)
    open: bool = Field(description=OPEN_FIELD)
    deadline_date: str | None = Field(description=DEADLINE_FIELD)


@tool(args_schema=ToolInput)
async def read_all_todos(collection_name: str):
    """Useful to gather all the user's to-dos."""
    try:
        repository = ToDoRepository(collection_name)
        return await repository.read_all()
    except Exception as e:
        return str(e)


@tool(args_schema=ToolInput)
async def clear_all_todos(collection_name: str):
    """Useful to clear all todos in collection"""
    try:
        repository = ToDoRepository(collection_name)
        return await repository.delete_all()
    except Exception as e:
        return str(e)


@tool(args_schema=ToDoInput)
async def add_todo(collection_name: str, content: str, open: bool, deadline_date: str | None = None):
    """Useful to add todos in collection"""
    try:
        repository = ToDoRepository(collection_name)
        to_do = ToDo(
            content=content,
            open=open,
            deadline_date=deadline_date
        )
        return await repository.create(to_do)
    except Exception as e:
        return str(e)
