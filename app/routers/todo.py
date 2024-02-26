from typing import Annotated

from fastapi import APIRouter, Depends
from ..mongodb import ToDoRepository, ToDo

router = APIRouter(
    prefix='/to-do'
)


@router.get('/get')
async def todo_get(repository: Annotated[ToDoRepository, Depends()]):
    return {'response': repository.db.name}


@router.post('/create')
async def todo_create(todo: ToDo, repository: Annotated[ToDoRepository, Depends()]):
    response = await repository.create(todo)
    return {'status': 'ok'}
