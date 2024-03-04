from contextlib import asynccontextmanager
from typing import Annotated

from dotenv import load_dotenv
from fastapi import APIRouter, Depends, status, FastAPI
from ..mongodb import (
    ToDoRepository,
    ToDo,
    MongoToDo,
    UpdateToDo,
    MongoToDoList,
    PyObjectId
)


@asynccontextmanager
async def lifespan(app: FastAPI):
    load_dotenv()
    yield

router = APIRouter(
    prefix='/to-do',
    lifespan=lifespan
)


@router.post(path='/create', status_code=status.HTTP_201_CREATED
)
async def todo_create(todo: ToDo, repository: Annotated[ToDoRepository, Depends()]) -> MongoToDo:
    return await repository.create(todo)


@router.get('/read/{item_id}')
async def todo_read(item_id: PyObjectId, repository: Annotated[ToDoRepository, Depends()]) -> MongoToDo:
    return await repository.read(item_id)


@router.get('/read-all')
async def todo_read_all(repository: Annotated[ToDoRepository, Depends()]) -> MongoToDoList:
    return await repository.read_all()


@router.put('/update/{item_id}')
async def todo_update(item_id: PyObjectId, todo: UpdateToDo,
                      repository: Annotated[ToDoRepository, Depends()]) -> MongoToDo:
    return await repository.update(item_id, todo)


@router.delete(path='/delete/{item_id}')
async def todo_delete(item_id: PyObjectId, repository: Annotated[ToDoRepository, Depends()]):
    return await repository.delete(item_id)


@router.delete(path='/delete-all')
async def todo_delete_all(repository: Annotated[ToDoRepository, Depends()]):
    return await repository.delete_all()
