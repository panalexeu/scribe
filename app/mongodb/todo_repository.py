from pymongo.results import InsertOneResult

from .repository import Repository
from .models import ToDo


class ToDoRepository(Repository):

    def __init__(self):
        self.collection = self.db.get_collection('to-do1')
        self.log()

    async def create(self, todo: ToDo):
        new_todo: InsertOneResult = await self.collection.insert_one(
            todo.model_dump()
        )

        created_todo = await self.collection.find_one(
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

    async def log(self):
        print(self.db.list_collection_names())
