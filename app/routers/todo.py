from typing import Annotated

from fastapi import APIRouter, Depends, status
from ..mongodb import ToDoRepository, ToDo, MongoToDo

router = APIRouter(
    prefix='/to-do'
)


@router.post(
    path='/create',
    status_code=status.HTTP_201_CREATED
)
async def todo_create(todo: ToDo, repository: Annotated[ToDoRepository, Depends()]) -> MongoToDo:
    return await repository.create(todo)


@router.get('/read/{item_id}')
async def todo_read(item_id: str, repository: Annotated[ToDoRepository, Depends()]) -> MongoToDo:
    return await repository.read(item_id)


@router.get('/read-all')
async def todo_read_all(repository: Annotated[ToDoRepository, Depends()]) -> list[MongoToDo]:
    return await repository.read_all()


@router.put('/update/{item_id}')
async def todo_update(item_id: str, repository: Annotated[ToDoRepository, Depends()]) -> MongoToDo:
    return await repository.update(item_id)


@router.delete('/delete/{item_id}')
async def todo_delete(item_id: str, repository: Annotated[ToDoRepository, Depends()]) -> MongoToDo:
    return await repository.delete(item_id)
