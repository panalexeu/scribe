from fastapi import APIRouter


router = APIRouter(
    prefix='todo'
)


@router.get('/')
async def todo_get():
    return {'response': 'to-do'}
