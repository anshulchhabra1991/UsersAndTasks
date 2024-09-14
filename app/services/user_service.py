from sqlalchemy.orm import Session
from ..models import user_models as models
from ..schema import user_schema as schema
from fastapi import HTTPException

def check_user_exists(db: Session, email: str, username: str):
    return db.query(models.User).filter(
        (models.User.email == email) | (models.User.username == username)
    ).first()

def create(db: Session, user: schema.UserCreate):
    try:
        existing_user = check_user_exists(db, user.email, user.username)
        if existing_user:
            raise HTTPException(status_code=400, detail="Username or email already exists.")
        db_user = models.User(username=user.username, email=user.email)
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))


def get_by_id(db: Session, user_id: int):
    try:
        user = db.query(models.User).filter(models.User.id == user_id).first()
        if not user:
            return None
        return user
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


def update(db: Session, user_id: int, user_update: schema.UserUpdate):
    try:
        user = db.query(models.User).filter(models.User.id == user_id).first()

        if not user:
            raise HTTPException(status_code=404, detail="User not found")

        if user_update.username:
            user.username = user_update.username
        if user_update.email:
            user.email = user_update.email

        db.commit()
        db.refresh(user)
        return user
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))

def delete(db: Session, user_id: int):
    try:
        user = db.query(models.User).filter(models.User.id == user_id).first()

        if not user:
            raise HTTPException(status_code=404, detail="User not found")

        db.delete(user)
        db.commit()
        return {"message": "User deleted successfully"}
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))

def list(db: Session, email: str = None, username: str = None):
    try:
        query = db.query(models.User)
        if email:
            query = query.filter(models.User.email == email)
        if username:
            query = query.filter(models.User.username == username)

        users = query.all()
        if not users:
            raise HTTPException(status_code=404, detail="User not found")
        return users
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
