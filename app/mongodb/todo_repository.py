from pymongo.results import InsertOneResult

from .repository import Repository
from .models import ToDo


class ToDoRepository(Repository):

    async def create(self, todo: ToDo) -> ToDo:
        await self.set_up_connection()  # connection with mongo db set up

        new_todo: InsertOneResult = await self.collection.insert_one(
            todo.model_dump(exclude='_id')
        )

        created_todo = await self.collection.find_one(
            {"_id": new_todo.inserted_id}
        )

        return ToDo(**created_todo)

    async def read(self):
        pass

    async def read_all(self):
        pass

    async def update(self):
        pass

    async def delete(self):
        pass
