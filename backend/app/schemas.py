"""
Models
================================================================================

!REMEMBER: If editing user model, mirror any new attributes in db.py User
class as well!

"""
from beanie import PydanticObjectId
from fastapi_users import schemas
from typing import Optional

class UserRead(schemas.BaseUser[PydanticObjectId]):
   is_adult: Optional[bool]

class UserCreate(schemas.BaseUserCreate):
   is_adult: Optional[bool]

class UserUpdate(schemas.BaseUserUpdate):
   is_adult: Optional[bool]
