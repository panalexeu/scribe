from pymongo import ReturnDocument
from pymongo.results import InsertOneResult, DeleteResult
from bson import ObjectId
from fastapi import HTTPException

from .repository import Repository
from .models import ToDo, MongoToDo, UpdateToDo, MongoToDoList


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

    async def read_all(self) -> MongoToDoList:
        await self.set_up_connection()

        found_todos = await self.collection.find().to_list(16)
        mongo_todos = MongoToDoList(todos=found_todos)

        return mongo_todos

    async def update(self, item_id: str, item: UpdateToDo) -> MongoToDo:
        await self.set_up_connection()

        todo_parsed = {key: value for key, value in item.model_dump().items() if value is not None}

        updated_student = await self.collection.find_one_and_update(
            {'_id': ObjectId(item_id)},
            {'$set': todo_parsed},
            return_document=ReturnDocument.AFTER
        )

        if updated_student is None:
            raise HTTPException(status_code=404, detail=f"Student {item_id} not found")

        return MongoToDo(**updated_student)

    async def delete(self, item_id: str):
        await self.set_up_connection()

        deleted_todo: DeleteResult = await self.collection.delete_one(
            {'_id': ObjectId(item_id)}
        )

        if deleted_todo.deleted_count != 1:
            raise HTTPException(status_code=404, detail=f"Student {item_id} not found")

        return {'response': 'to-do deleted'}

    async def delete_all(self):
        await self.set_up_connection()

        await self.collection.delete_many({})

        return {'response': 'to-dos cleared.'}
