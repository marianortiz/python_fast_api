from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from app.config.database import SessionLocal
from . import repository, schema

router = APIRouter()


def get_db():  # Dependencies
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Create User
@router.post("/users", response_model=schema.User, status_code=status.HTTP_201_CREATED, tags=['USER'])
async def create_user(user: schema.CreateUser, db: Session = Depends(get_db)):
    try:
        return repository.create_user(db=db, user=user)
    except HTTPException as ex:
        raise HTTPException(status_code=ex.status_code, detail=ex.detail)


# Listar Users
@router.get("/users", response_model=List[schema.User], tags=['USER'])
async def get_all_users(db: Session = Depends(get_db)):
    try:
        return repository.fetch_all(db=db)
    except HTTPException as ex:
        raise HTTPException(status_code=ex.status_code, detail=ex.detail)


# Listar User
@router.get("/users/{username}", response_model=schema.User,  tags=['USER'])
async def get_user(username: str, db: Session = Depends(get_db)):
    try:
        user = repository.get_user_by_username(db=db, username=username)
        if user is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="user: {} not found".format(username))
        return user
    except HTTPException as ex:
        raise HTTPException(status_code=ex.status_code, detail=ex.detail)


# Modificar User
@router.put("/users/{username}", response_model=schema.User,  tags=['USER'])
async def update_user(username: str, user: schema.UpdateUser, db: Session = Depends(get_db)):
    try:
        return repository.update_user(db=db, username=username, user=user)
    except HTTPException as ex:
        raise HTTPException(status_code=ex.status_code, detail=ex.detail)
