from contextlib import asynccontextmanager
from typing import Annotated

from dotenv import load_dotenv
from fastapi import APIRouter, Depends, FastAPI

from ..agent import Prompt, Scribe


@asynccontextmanager
async def lifespan(app: FastAPI):
    load_dotenv()
    yield


router = APIRouter(
    prefix='/scribe',
    lifespan=lifespan
)


@router.post('/ask')
async def ask(prompt: Prompt, scribe: Annotated[Scribe, Depends()], collection_name: str = 'to-do'):
    return await scribe.ask(prompt.prompt, collection_name)
