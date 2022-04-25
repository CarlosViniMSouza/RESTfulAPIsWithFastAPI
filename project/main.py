from fastapi import FastAPI
from typing import List
from uuid import UUID

from models import User, Gender, Role

app = FastAPI()

db: List[User] = [
    User(
        # id=uuid4(), -> generate a random id for each user
        id=UUID("cec1889b-1068-45c3-b716-534c0b09c1b5"),
        first_name="Carlos",
        last_name="Souza",
        gender=Gender.male,
        role=[Role.admin]
    ),

    User(
        id=UUID("a00bc999-a424-4f94-a785-86ef0547fc5d"),
        first_name="Jam",
        last_name="Silver",
        gender=Gender.female,
        role=[Role.student, Role.user]
    ),

    User(
        id=UUID("495eea4c-1334-49fb-afa9-4360f54e1ca2"),
        first_name="Will",
        last_name="Storne",
        gender=Gender.male,
        role=[Role.user]
    ),
]


@app.get("/")
async def welcome():
    return {"message": "Welcome to my API building in FastAPI"}


@app.get("/api/v1/users")
async def fetch_users():
    return db
