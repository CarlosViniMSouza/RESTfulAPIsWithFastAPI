from typing import Optional, List
from pydantic import BaseModel
from uuid import UUID, uuid4
from enum import Enum


class Role(str, Enum):
    admin = "admin"
    user = "user"
    student = "student"


class Gender(str, Enum):
    male = "male"
    female = "female"


class User(BaseModel):
    id: Optional[UUID] = uuid4()
    first_name: str
    last_name: str
    middle_name: Optional[str]
    gender: Gender
    role: List[Role]


class UserPutReq(BaseModel):
    first_name: Optional[str]
    last_name: Optional[str]
    middle_name: Optional[str]
    role: Optional[List[Role]]
