from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from ..services import user_service
from ..schema import user_schema as schema
from ..config.database import get_db
from typing import Optional

router = APIRouter()

@router.post("/user/", response_model=schema.UserCreate)
def create_user(user: schema.UserCreate, db: Session = Depends(get_db)):
        return  user_service.create(db=db, user=user)

@router.get("/user/{user_id}", response_model=schema.UserResponse)
def get_user(user_id: int, db: Session = Depends(get_db)):
    userDetails = user_service.get_by_id(db, user_id)
    if not userDetails:
        raise HTTPException(status_code=404, detail="User not found")

@router.put("/user/{user_id}", response_model=schema.UserResponse)
def update_user(user_id: int, user_update: schema.UserUpdate, db: Session = Depends(get_db)):
    return user_service.update(db=db, user_id=user_id, user_update=user_update)

@router.delete("/user/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    return user_service.delete(db=db, user_id=user_id)

@router.get("/users", response_model=list[schema.UserResponse])
def search_user(
        email: Optional[str] = Query(None),
        username: Optional[str] = Query(None),
        db: Session = Depends(get_db)
):
    return user_service.list(db=db, email=email, username=username)