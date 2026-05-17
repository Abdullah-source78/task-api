from fastapi import FastAPI, Depends , HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session
from database import SessionLocal, engine ,Base
from models.task import TaskDB
from routers.auth import router as auth_router
from fastapi.security import OAuth2PasswordBearer
from auth.jwt_handler import verify_token
from models.user import User

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
        from_attributes = True


oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="/login"
)

def get_current_user(
    token: str = Depends(oauth2_scheme)
):
    payload = verify_token(token)

    if payload is None:
        raise HTTPException(
            status_code=401,
            detail="Invalid token"
        )

    return payload


@app.get("/me")
def get_me(
    current_user: dict = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    username = current_user.get("sub")

    user = db.query(User).filter(
        User.username == username
    ).first()

    return {
        "id": user.id,
        "username": user.username,
        "email": user.email
    }


# 🔹 Routes
@app.get("/", tags=["Health"])
def home():
    return {"message": "Docker-API is working"}


@app.get("/tasks", response_model=list[TaskResponse])
def get_tasks(
    current_user: dict = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    username = current_user.get("sub")

    user = db.query(User).filter(
        User.username == username
    ).first()

    return db.query(TaskDB).filter(
        TaskDB.user_id == user.id
    ).all()


@app.post("/tasks", response_model=TaskResponse)
def create_task(
    task: TaskCreate,
    current_user: dict = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    username = current_user.get("sub")

    user = db.query(User).filter(
        User.username == username
    ).first()

    new_task = TaskDB(
        title=task.title,
        completed=task.completed,
        user_id=user.id
    )

    db.add(new_task)
    db.commit()
    db.refresh(new_task)

    return new_task


@app.put("/tasks/{task_id}", response_model=TaskResponse)
def update_task(
    task_id: int,
    updated_task: TaskUpdate,
    current_user: dict = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    username = current_user.get("sub")

    user = db.query(User).filter(
        User.username == username
    ).first()

    task = db.query(TaskDB).filter(
        TaskDB.id == task_id
    ).first()

    if not task:
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )

    if task.user_id != user.id:
        raise HTTPException(
            status_code=403,
            detail="Not authorized"
        )

    task.title = updated_task.title
    task.completed = updated_task.completed

    db.commit()
    db.refresh(task)

    return task

@app.delete("/tasks/{task_id}")
def delete_task(
    task_id: int,
    current_user: dict = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    username = current_user.get("sub")

    user = db.query(User).filter(
        User.username == username
    ).first()

    task = db.query(TaskDB).filter(
        TaskDB.id == task_id
    ).first()

    if not task:
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )

    if task.user_id != user.id:
        raise HTTPException(
            status_code=403,
            detail="Not authorized"
        )

    db.delete(task)
    db.commit()

    return {
        "message": "Task deleted"
    }