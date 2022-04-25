from fastapi import FastAPI
from typing import List
from uuid import uuid4

from project.models import User, Gender, Role

app = FastAPI()

db: List[User] = [
    User(
        id=uuid4(),
        first_name="Carlos",
        last_name="Souza",
        gender=Gender.male,
        role=[Role.admin]
    ),

    User(
        id=uuid4(),
        first_name="Jam",
        last_name="Silver",
        gender=Gender.female,
        role=[Role.student, Role.user]
    ),

    User(
        id=uuid4(),
        first_name="Will",
        last_name="Storne",
        gender=Gender.male,
        role=[Role.user]
    ),
]


@app.get("/")
async def welcome():
    return {"message": "Welcome to my API building in FastAPI"}
