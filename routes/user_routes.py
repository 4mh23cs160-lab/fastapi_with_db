from fastapi import APIRouter
from sqlalchemy.orm import Session
from fastapi import Depends
from db import get_db
from repositories.user_repo import UserRepo
from schemas.user_schemas import UserSchema
router = APIRouter()

@router.post("/signup")
def signup():
    return {"message": "User signed up successfully"}

@router.post("/login")
def login():
    return {"message": "User logged in successfully"}