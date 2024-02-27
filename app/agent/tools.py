from langchain.pydantic_v1 import BaseModel, Field
from langchain.tools import tool

from ..mongodb import ToDoRepository, MongoToDoList


class ToolInput(BaseModel):
    collection_name: str = Field(description='In this parameter collection_name should be provided.')


@tool(args_schema=ToolInput)
async def read_all_todos(collection_name: str) -> MongoToDoList:
    """Useful to gather all the user's to-dos."""
    repository = ToDoRepository(collection_name)
    return await repository.read_all()
