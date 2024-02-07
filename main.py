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

@app.get("/tasks")
def get_tasks():
    return tasks

@app.get("/tasks/{task_id}")
def get_task(task_id: int):
    for task in tasks:
        if task["id"] == task_id:
            return task
    raise HTTPException(status_code=404, detail="Task not found")

@app.post("/tasks")
def add_task(task: Task):
    new_task = {
        "id": len(tasks) + 1,
        "text": task.text,
        "day": task.day,
        "reminder": task.reminder,
    }
    tasks.append(new_task)
    return new_task

@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    global tasks
    tasks = [task for task in tasks if task["id"] != task_id]
    return {"message": "Task deleted successfully"}