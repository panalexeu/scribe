from typing import Annotated

from fastapi import APIRouter, Depends
from ..mongodb import ToDoRepository

router = APIRouter(
    prefix='/to-do'
)


@router.get('/get')
async def todo_get(repository: Annotated[ToDoRepository, Depends()]):
    return {'response': repository.db.name}
