from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import SessionLocal
from models.user import User
from schemas.user import UserCreate , UserLogin
from auth.password import hash_password
from auth.password import verify_password
from auth.jwt_handler import create_access_token
from fastapi.security import OAuth2PasswordRequestForm

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/register" , tags=["Register"])
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


@router.post("/login" , include_in_schema=False)
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):
    db_user = db.query(User).filter(
        User.username == form_data.username
    ).first()

    if not db_user:
        return {"error": "Invalid username"}

    valid_password = verify_password(
        form_data.password,
        db_user.hashed_password
    )

    if not valid_password:
        return {"error": "Invalid password"}

    access_token = create_access_token(
        data={"sub": db_user.username}
    )

    return {
        "access_token": access_token,
        "token_type": "bearer"
    }