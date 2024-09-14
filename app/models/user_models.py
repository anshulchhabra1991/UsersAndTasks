from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from ..config.database import Database

Base = Database().Base

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, index=True)
    email = Column(String(100), unique=True)

    tasks = relationship("Task", back_populates="user", foreign_keys="[Task.user_id]")
    created_tasks = relationship("Task", back_populates="creator", foreign_keys="[Task.created_by]")
