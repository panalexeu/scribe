

from pydantic import BaseModel, Field
from bson import ObjectId


class ToDo(BaseModel):
    id: str
