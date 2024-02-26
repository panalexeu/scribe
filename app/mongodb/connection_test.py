import os

from motor.motor_asyncio import AsyncIOMotorClient


async def ping_server():
    client = AsyncIOMotorClient(os.environ.get('MONGODB_URL'))

    try:
        await client.admin.command('ping')
        return "Pinged deployment. Successfully connected to MongoDB!"
    except Exception as e:
        print(e)
