from pymongo.errors import CollectionInvalid
from pymongo.results import InsertOneResult

from .repository import Repository
from .models import ToDo


class ToDoRepository(Repository):

    def __init__(self):
        pass

    async def get_collection(self):
        try:
            await self.db.create_collection('to-do')
        except CollectionInvalid:
            pass  # Collection already exists

        return self.db.get_collection('to-do')

    async def create(self, todo: ToDo):
        collection = await self.get_collection()

        new_todo: InsertOneResult = await collection.insert_one(
            todo.model_dump()
        )

        created_todo = await collection.find_one(
            {"_id": new_todo.inserted_id}
        )

        return created_todo

    async def read(self):
        pass

    async def read_all(self):
        pass

    async def update(self):
        pass

    async def delete(self):
        pass
