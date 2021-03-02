from fastapi import FastAPI

from app.db import engine
from app.db.base_model import BaseModel


async def connect_to_db(app: FastAPI):
    BaseModel.metadata.create_all(bind=engine)
    await database.connect()


async def close_db_connection(app: FastAPI):
    pass
