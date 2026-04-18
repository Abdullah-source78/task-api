from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from typing import Optional
from database import SessionLocal
from models import TaskDB

app = FastAPI()


class TaskCreate(BaseModel):
    title: str
    completed: bool = False

class Task(BaseModel):
    id: int
    title: str
    completed: bool = False


class TaskUpdate(BaseModel):
    title: str
    completed: bool

@app.get("/")
def home():
    return {"message": "API is working"}

@app.get("/tasks")
def get_tasks():
    db = SessionLocal()
    tasks = db.query(TaskDB).all()
    return tasks



@app.post("/tasks")
def create_task(task: TaskCreate):

    try:
        db = SessionLocal()

        new_task = TaskDB(
            title=task.title,
            completed=task.completed
        )

        db.add(new_task)
        db.commit()
        db.refresh(new_task)
    finally:
        db.close()

    return new_task

@app.put("/tasks/{task_id}")
def update_task(task_id: int, updated_task: TaskUpdate):
    try:
        db = SessionLocal()

        task = db.query(TaskDB).filter(TaskDB.id == task_id).first()

        if not task:
            return {"error": "Task not found"}

        task.title = updated_task.title
        task.completed = updated_task.completed

        db.commit()
        db.refresh(task)
    finally:
        db.close()

    return task

app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    try:
        db = SessionLocal()
        task = db.query(TaskDB).filter(TaskDB.id == task_id).first()

        if not task:
            return {"error": "Task not found"}

        db.delete(task)
        db.commit()
    finally:
        db.close()
    return {"message": "Task deleted"}
