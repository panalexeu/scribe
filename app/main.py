from fastapi import FastAPI
from mangum import Mangum

from .routers import health, todo

app = FastAPI(root_path='/scribe')
app.include_router(health.router)
app.include_router(todo.router)

health_handler = Mangum(health.router)
todo_handler = Mangum(todo.router)
