from fastapi import FastAPI

from app.db import database, BaseModel, engine


async def connect_to_db(app: FastAPI):
    BaseModel.metadata.create_all(bind=engine)
    await database.connect()
