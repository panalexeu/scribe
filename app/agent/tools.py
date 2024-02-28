from datetime import datetime

from langchain.pydantic_v1 import BaseModel, Field
from langchain.tools import tool

from .prompt_template import (
    DESCRIPTION_FIELD,
    CONTENT_FIELD,
    OPEN_FIELD,
    DEADLINE_FIELD,
    ID_FIELD,
    CONTENT_FIELD_UPDATE,
    OPEN_FIELD_UPDATE
)
from ..mongodb import ToDoRepository, ToDo, UpdateToDo


class ToolInput(BaseModel):
    collection_name: str = Field(description=DESCRIPTION_FIELD)


class ToDoInput(ToolInput):
    content: str = Field(description=CONTENT_FIELD)
    open: bool = Field(description=OPEN_FIELD)
    deadline_date: str | None = Field(description=DEADLINE_FIELD)


class ToDoIdInput(ToolInput):
    id: str = Field(description=ID_FIELD)


class ToDoInputUpdate(ToDoIdInput):
    content: str | None = Field(description=CONTENT_FIELD_UPDATE)
    open: bool | None = Field(description=OPEN_FIELD_UPDATE)
    deadline_date: str | None = Field(description=DEADLINE_FIELD)


@tool(args_schema=ToolInput)
async def read_all_todos(collection_name: str):
    """Useful to gather/provide/list all the user's to-dos.
    If the user doesn't mention any format instructions on how he wants to see the returned to-dos,  provide to-dos in
    the following way without any numeration:
    * Task: content
        - Open: open
        - Creation_date: creation-date (specify date and hours only not seconds)
        - Deadline_date: deadline-date (specify date and hours only not seconds)
    """
    try:
        repository = ToDoRepository(collection_name)
        return await repository.read_all()
    except Exception as e:
        return str(e)


@tool(args_schema=ToDoInputUpdate)
async def update_todo(
        collection_name: str,
        id: str,
        content: str = None,
        open: bool = None,
        deadline_date: str = None
):
    """Useful to update a single to-do. Before calling this tool always call read_all_todos tool to get to-dos with
    their ids. Never change retrieved to-dos ids"""
    try:
        repository = ToDoRepository(collection_name)
        return await repository.update(
            item_id=id,
            item=UpdateToDo(
                content=content,
                open=open,
                deadline_date=deadline_date
            )
        )
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


@tool(args_schema=ToDoIdInput)
async def delete_todo(collection_name: str, id: str):
    """Useful to delete a single to-do. Before calling this tool always call read_all_todos tool to get to-dos with
    their ids. Never change retrieved to-dos ids"""
    try:
        repository = ToDoRepository(collection_name)
        return await repository.delete(id)
    except Exception as e:
        return str(e)


@tool(args_schema=ToDoInput)
async def add_todo(collection_name: str, content: str, open: bool, deadline_date: str | None = None):
    """Useful to add to-dos in collection. Before calling this tool always call get_curr_time tool"""
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


@tool
def get_curr_time():
    """Useful to retrieve current time and resolve tasks related to time management"""
    return datetime.today()
