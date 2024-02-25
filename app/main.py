from contextlib import asynccontextmanager

from fastapi import FastAPI
from mangum import Mangum
from dotenv import load_dotenv

from .routers import health, todo


@asynccontextmanager
async def lifespan(app: FastAPI):
    load_dotenv()
    yield


app = FastAPI(root_path='/scribe', lifespan=lifespan)
app.include_router(health.router)
app.include_router(todo.router)

health_handler = Mangum(health.router)
todo_handler = Mangum(todo.router)
