from typing import Annotated
from sqlmodel import SQLModel, create_engine, Session
from fastapi import Depends
from models.task_model import Task
from models.user_models import User

engine = create_engine("sqlite:///task.db",  echo=True)
SQLModel.metadata.create_all(engine)
def get_session():
    with Session(engine) as session:
        yield session

SessionDepends = Annotated[Session, Depends(get_session)]

