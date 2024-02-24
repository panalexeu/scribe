from fastapi import APIRouter


router = APIRouter(
    prefix='/to-do'
)


@router.get('/get')
async def todo_get():
    return {'response': 'to-do'}
