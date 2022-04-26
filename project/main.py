from fastapi import FastAPI, HTTPException
from typing import List
from uuid import UUID

from models import User, Gender, Role
from project.models import UserPutReq

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


@app.post("/api/v1/users")
async def register_user(user: User):
    db.append(user)
    return {"id": user.id}


@app.put("/api/v1/users/{id_user}")
async def update_user(up_user: UserPutReq, id_user: UUID):
    for user in db:
        if (user.id == id_user):
            if (up_user.first_name is not None):
                user.first_name = up_user.first_name
            if (up_user.last_name is not None):
                user.last_name = up_user.last_name
            if (up_user.middle_name is not None):
                user.middle_name = up_user.middle_name
            if (up_user.role is not None):
                user.role = up_user.role


@app.delete("/api/v1/users/{id_user}")
async def delete_user(id_user: UUID):
    for user in db:
        if user.id == id_user:
            db.remove(user)
            return {"message": f"user of id: {id_user} -> deleted"}

        raise HTTPException(
            status_code=404,
            detail=f"user of id: {id_user} -> doesnt exist"
        )
