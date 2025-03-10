from fastapi import APIRouter, Depends
from models import User
from sqlalchemy.orm import Session
from pydantic import BaseModel
from db import get_db

router = APIRouter()

class UserCreate(BaseModel):
    email: str
    password_hash: str
    public_key: str

@router.post("/")
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = User(**user.dict())
    db.add(db_user)
    db.commit()
    return {"msg": "User created!"}
