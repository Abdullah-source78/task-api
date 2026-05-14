from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import SessionLocal
from models.user import User
from schemas.user import UserCreate , UserLogin
from auth.password import hash_password
from auth.password import verify_password
from auth.jwt_handler import create_access_token

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/register")
def register(
    user: UserCreate,
    db: Session = Depends(get_db)
):
    print(user.password)
    print(type(user.password))
    print(len(user.password))
    hashed_pw = hash_password(user.password)

    new_user = User(
        username=user.username,
        email=user.email,
        hashed_password=hashed_pw
    )
    

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {
        "message": "User created successfully"
    }

@router.post("/login")
def login(
    user: UserLogin,
    db: Session = Depends(get_db)
):
    db_user = db.query(User).filter(
        User.username == user.username
    ).first()

    if not db_user:
        return {
            "error": "Invalid username"
        }

    valid_password = verify_password(
        user.password,
        db_user.hashed_password
    )

    if not valid_password:
        return {
            "error": "Invalid password"
        }

    access_token = create_access_token(
        data={
            "sub": db_user.username
        }
    )

    return {
        "access_token": access_token,
        "token_type": "bearer"
    }