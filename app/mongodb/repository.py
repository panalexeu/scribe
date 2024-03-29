import os
from abc import ABC, abstractmethod

from pydantic import BaseModel
from motor.motor_asyncio import AsyncIOMotorClient
from pymongo.errors import CollectionInvalid

from .models import MongoModel, PyObjectId


class Repository(ABC):
    collection = None
    db = None
    client = None

    def __init__(self, collection_name: str = 'to-do'):  # to-do for now
        self.collection_name = collection_name

    # Before any CRUD operation this method should be called to set up connection with MongoDB. It is impossible to set
    # up connection in __init__ because it is synchronous, that's why this method is needed.
    async def set_up_connection(self):
        self.client = AsyncIOMotorClient(os.environ.get('MONGODB_URL'))
        self.db = self.client.get_database('scribe')

        # if collection doesn't exist a new one is created
        try:
            await self.db.create_collection(
                self.collection_name,
                check_exists=True,
                capped=True,
                max=16,
                size=4000  # in bytes
            )
        except CollectionInvalid:
            pass

        self.collection = self.db.get_collection(self.collection_name)

    async def log(self):
        collections = await self.db.list_collection_names()
        dbs = await self.client.list_database_names()

        print('Databases: ' + str(dbs))
        print(f'Collections of {self.db.name}: ' + str(collections))

    @abstractmethod
    async def create(self, item: BaseModel) -> MongoModel:
        pass

    @abstractmethod
    async def read(self, item_id: PyObjectId) -> MongoModel:
        pass

    @abstractmethod
    async def read_all(self) -> list[MongoModel]:
        pass

    @abstractmethod
    async def update(self, item_id: PyObjectId, item: BaseModel) -> MongoModel:
        pass

    @abstractmethod
    async def delete(self, item_id: PyObjectId):
        pass

    @abstractmethod
    async def delete_all(self):
        pass
