# main.py

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

origins = ["http://localhost:5173"] 

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Task(BaseModel):
    text: str
    day: str
    reminder: bool

tasks = [
    {
        "id": 1,
        "text": "dr appointment",
        "day": "March 1st at 2:30p",
        "reminder": True,
    },
    {
        "id": 2,
        "text": "gym",
        "day": "March 1st at 2:30p",
        "reminder": True,
    },
    {
        "id": 3,
        "text": "walk dog",
        "day": "March 1st at 2:30p",
        "reminder": False,
    },
]

@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI!"}