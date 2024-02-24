from fastapi import FastAPI
from mangum import Mangum

import health
import todo


app = FastAPI()
app.include_router(health.router)
app.include_router(todo.router)

health_handler = Mangum(health.router)
todo_handler = Mangum(todo.router)
