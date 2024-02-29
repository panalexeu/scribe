from contextlib import asynccontextmanager

from dotenv import load_dotenv
from fastapi import APIRouter, FastAPI

from ..mongodb import ping_server


@asynccontextmanager
async def lifespan(app: FastAPI):
    load_dotenv()
    yield


router = APIRouter(
    prefix='/health',
    lifespan=lifespan
)


@router.get('/get')
async def health():
    response = await ping_server()
    return {'response': response}


@router.get('/simple-get')
async def health_simple_get():
    return {'response': 'ok'}
