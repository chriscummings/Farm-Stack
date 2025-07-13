"""
Database Config
================================================================================

"""

import os
#
import motor.motor_asyncio
from beanie import Document
from fastapi_users.db import BeanieBaseUser
from fastapi_users_db_beanie import BeanieUserDatabase
from typing import Optional
from pydantic import Field


MONGO_USERNAME = os.environ["MONGO_USERNAME"]
MONGO_PASSWORD = os.environ["MONGO_PASSWORD"]
MONGO_DATABASE = os.environ["MONGO_DATABASE"]
MONGO_PORT = os.environ["MONGO_PORT"]
DATABASE_URL = f'mongodb://{MONGO_USERNAME}:{MONGO_PASSWORD}@mongo:{MONGO_PORT}'

client = motor.motor_asyncio.AsyncIOMotorClient(
    DATABASE_URL, uuidRepresentation="standard"
)
db = client[MONGO_DATABASE]


class User(BeanieBaseUser, Document):
    is_adult: Optional[bool] = Field(default=False)

async def get_user_db():
    yield BeanieUserDatabase(User)