import os

from motor.motor_asyncio import AsyncIOMotorClient


async def ping_server():
    uri = os.environ.get('MONGODB_URL')

    client = AsyncIOMotorClient(uri)

    try:
        await client.admin.command('ping')
        return "Pinged your deployment. Successfully connected to MongoDB!"
    except Exception as e:
        print(e)
