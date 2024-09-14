from sqlalchemy.orm import Session
from ..models import task_models as models
from ..schema import task_schema as schema
from fastapi import HTTPException

def create(db: Session, task: schema.TaskCreate):
    try:
        db_task = models.Task(
            status=task.status,
            user_id=task.for_user_id,
            created_by=task.from_user_id
        )
        db.add(db_task)
        db.commit()
        db.refresh(db_task)
        return db_task
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))

def tasks(db: Session, user_id: int):
    try:
        query = db.query(models.Task).filter(models.Task.user_id == user_id)
        return query.all()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


def update(db: Session, task_id: int, created_by: int):
    try:
        task = db.query(models.Task).filter(
            models.Task.id == task_id,
            models.Task.created_by == created_by
        ).first()

        if not task:
            raise HTTPException(status_code=500, detail='Task not found or Owner mismatch!')

        task.status = schema.TaskStatus.COMPLETE
        db.commit()
        db.refresh(task)
        return task
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))