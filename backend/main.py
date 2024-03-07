from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import requests

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class User(BaseModel):
    username: str


PRIVATE_KEY = "77d37a7f-d879-4222-be23-24ea32a62a0b"


@app.post("/authenticate")
async def authenticate(user: User):
    response = requests.put(
        "https://api.chatengine.io/users/",
        data={
            "username": user.username,
            "secret": user.username,
            "first_name": user.username,
        },
        headers={"Private-key": PRIVATE_KEY},
    )
    return response.json()
