from fastapi import FastAPI, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session
from database import SessionLocal, engine ,Base
from models.task import TaskDB
from routers.auth import router as auth_router

Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(auth_router)



# 🔹 DB Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# 🔹 Pydantic Schemas
class TaskCreate(BaseModel):
    title: str
    completed: bool = False


class TaskUpdate(BaseModel):
    title: str
    completed: bool


# ✅ Response Model (ONLY ONE)
class TaskResponse(BaseModel):
    id: int
    title: str
    completed: bool

    class Config:
        orm_mode = True


# 🔹 Routes
@app.get("/", tags=["Health"])
def home():
    return {"message": "Nginx-API is working"}


@app.get("/tasks", response_model=list[TaskResponse])
def get_tasks(db: Session = Depends(get_db)):
    return db.query(TaskDB).all()


@app.post("/tasks", response_model=TaskResponse)
def create_task(task: TaskCreate, db: Session = Depends(get_db)):
    new_task = TaskDB(
        title=task.title,
        completed=task.completed
    )
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return new_task


@app.put("/tasks/{task_id}", response_model=TaskResponse)
def update_task(task_id: int, updated_task: TaskUpdate, db: Session = Depends(get_db)):
    task = db.query(TaskDB).filter(TaskDB.id == task_id).first()

    if not task:
        return {"error": "Task not found"}

    task.title = updated_task.title
    task.completed = updated_task.completed

    db.commit()
    db.refresh(task)
    return task


@app.delete("/tasks/{task_id}")
def delete_task(task_id: int, db: Session = Depends(get_db)):
    task = db.query(TaskDB).filter(TaskDB.id == task_id).first()

    if not task:
        return {"error": "Task not found"}

    db.delete(task)
    db.commit()
    return {"message": "Task deleted"}

