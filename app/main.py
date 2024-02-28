import os
from contextlib import asynccontextmanager

from fastapi import FastAPI
from mangum import Mangum
from dotenv import load_dotenv
from starlette.middleware.sessions import SessionMiddleware

from .routers import health, todo, agent, auth


@asynccontextmanager
async def lifespan(app: FastAPI):
    load_dotenv()
    yield


app = FastAPI(lifespan=lifespan)

app.add_middleware(SessionMiddleware, secret_key=os.environ.get('SECRET_KEY'))

app.include_router(health.router)
app.include_router(todo.router)
app.include_router(agent.router)
app.include_router(auth.router)

app_handler = Mangum(app)
health_handler = Mangum(health.router)
todo_handler = Mangum(todo.router)
agent_handler = Mangum(agent.router)
auth_handler = Mangum(agent.router)

