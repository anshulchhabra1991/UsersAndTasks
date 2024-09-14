from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from app.api import users
from app.api import tasks
from app.middlewares.authentication import AuthenticationMiddleware

app = FastAPI()

app.add_middleware(AuthenticationMiddleware)

app.include_router(users.router, prefix="/api/v1")
app.include_router(tasks.router, prefix="/api/v1")


