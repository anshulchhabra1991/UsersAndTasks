from pydantic import BaseModel
from typing import Optional
from enum import Enum

class TaskStatus(str, Enum):
    INIT = "init"
    COMPLETE = "complete"

class TaskCreate(BaseModel):
    status: TaskStatus
    from_user_id: int
    for_user_id: int

class TaskResponse(BaseModel):
    id: int
    status: TaskStatus
    user_id: int
    created_by: int

    class Config:
        orm_mode = True
