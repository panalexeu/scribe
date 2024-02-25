import os
from abc import ABC, abstractmethod

from pydantic import BaseModel
from motor.motor_asyncio import AsyncIOMotorClient


class Repository(ABC):
    client = AsyncIOMotorClient(os.environ.get('MONGODB_URL'))
    db = client.get_database('scribe')
    collection = None

    @abstractmethod
    async def create(self, item: BaseModel):
        pass

    @abstractmethod
    async def read(self):
        pass

    @abstractmethod
    async def read_all(self):
        pass

    @abstractmethod
    async def update(self):
        pass

    @abstractmethod
    async def delete(self):
        pass
