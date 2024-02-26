from pymongo.results import InsertOneResult
from bson import ObjectId

from .repository import Repository
from .models import ToDo, MongoToDo, MongoModel


class ToDoRepository(Repository):

    async def create(self, todo: ToDo) -> MongoToDo:
        await self.set_up_connection()  # connection with mongo db set up

        new_todo: InsertOneResult = await self.collection.insert_one(
            todo.model_dump(exclude='_id')
        )

        created_todo = await self.collection.find_one(
            {'_id': new_todo.inserted_id}
        )

        return MongoToDo(**created_todo)

    async def read(self, item_id: str) -> MongoToDo:
        await self.set_up_connection()

        found_todo = await self.collection.find_one(
            {'_id': ObjectId(item_id)}
        )

        return MongoToDo(**found_todo)

    async def read_all(self) -> list[MongoToDo]:
        await self.set_up_connection()

    async def update(self, item_id: str) -> MongoToDo:
        await self.set_up_connection()

    async def delete(self, item_id: str) -> MongoToDo:
        await self.set_up_connection()
