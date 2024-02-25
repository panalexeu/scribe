from datetime import datetime
from enum import Enum

from pydantic import BaseModel, Field


class ToDoStatusEnum(Enum):
    OPEN = 'OPEN'
    CLOSED = 'CLOSED'


class ToDo(BaseModel):
    id: str
    content: str = Field(min_length=1, max_length=128)
    status: ToDoStatusEnum = ToDoStatusEnum.OPEN
    creation_time: str = Field(default_factory=lambda: str(datetime.now().date()))
    deadline_time: str = Field(pattern='^(?:\d{4})-(?:0[1-9]|1[0-2])-(?:0[1-9]|[1-2][0-9]|3[0-1])$')
