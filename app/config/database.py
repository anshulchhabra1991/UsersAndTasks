from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from typing import Generator

class Database:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Database, cls).__new__(cls)
            DATABASE_URL = os.getenv('DATABASE_URL')
            cls._engine = create_engine(DATABASE_URL)
            cls._SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=cls._engine)
            cls._Base = declarative_base()
        return cls._instance

    @property
    def engine(self):
        return self._engine

    @property
    def SessionLocal(self):
        return self._SessionLocal

    @property
    def Base(self):
        return self._Base

def get_db() -> Generator:
    db = Database().SessionLocal()
    try:
        yield db
    finally:
        db.close()
