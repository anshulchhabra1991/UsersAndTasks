from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from ..services import user_service
from ..services import task_service
from ..schema import task_schema as schema
from ..config.database import get_db
from typing import Optional

router = APIRouter()

@router.post("/task/", response_model=schema.TaskResponse)
def add_task(task: schema.TaskCreate, db: Session = Depends(get_db)):
        if task.from_user_id == task.for_user_id:
                raise HTTPException(status_code=400, detail="from_user_id cannot be the same as for_user_id")

        from_user = user_service.get_by_id(db, task.from_user_id)
        to_user = user_service.get_by_id(db, task.for_user_id)

        if not from_user or not to_user:
                raise HTTPException(status_code=404, detail="One or both of the provided user IDs do not exist")

        return task_service.create(db, task)

@router.get("/tasks/{user_id}", response_model=list[schema.TaskResponse])
def get_tasks_for_user(user_id: int, db: Session = Depends(get_db)):
        tasks = task_service.tasks(db, user_id)
        if not tasks:
                raise HTTPException(status_code=404, detail="No tasks found for the user")
        return tasks

@router.put("/update/{task_id}/{created_by}", response_model=schema.TaskResponse)
def update_task_status(task_id: int, created_by: int, db: Session = Depends(get_db)):
        return task_service.update(db, task_id, created_by)