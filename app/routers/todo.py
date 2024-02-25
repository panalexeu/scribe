import os
from typing import Annotated

from fastapi import APIRouter, Depends
from ..mongodb import Repository

router = APIRouter(
    prefix='/to-do'
)


@router.get('/get')
async def todo_get(repository: Annotated[Repository, Depends()]):
    return {'response': repository.mongodb_url}
