from sqlalchemy import Column, Integer, ForeignKey, Enum
from sqlalchemy.orm import relationship
from enum import Enum as PyEnum
from ..config.database import Database

Base = Database().Base

class TaskStatus(PyEnum):
    INIT = "init"
    COMPLETE = "complete"

class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    status = Column(Enum(TaskStatus), default=TaskStatus.INIT)
    user_id = Column(Integer, ForeignKey("users.id"))
    created_by = Column(Integer, ForeignKey("users.id"))

    user = relationship("User", back_populates="tasks", foreign_keys=[user_id])
    creator = relationship("User", back_populates="created_tasks", foreign_keys=[created_by])
