from fastapi import APIRouter

from ..mongodb import ping_server

router = APIRouter(
    prefix='/health'
)


@router.get('/get')
async def health():
    response = await ping_server()
    return {'response': response}


@router.get('/simple-get')
async def health_simple_get():
    return {'response': 'ok'}
