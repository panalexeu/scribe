import os
from abc import ABC, abstractmethod

from motor.motor_asyncio import AsyncIOMotorClient


class Repository(ABC):
    client = AsyncIOMotorClient(os.environ.get('MONGODB_URL'))
    db = client.get_database('scribe')
    collection = None

    @abstractmethod
    def create(self):
        pass

    @abstractmethod
    def read(self):
        pass

    @abstractmethod
    def read_all(self):
        pass

    @abstractmethod
    def update(self):
        pass

    @abstractmethod
    def delete(self):
        pass
