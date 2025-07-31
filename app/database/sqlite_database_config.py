from typing import Annotated
from sqlmodel import SQLModel, create_engine, Session
from fastapi import Depends

engine = create_engine("sqlite:///task.db")
SQLModel.metadata.create_all(engine)
def get_session():
    with Session(engine) as session:
        yield session

SessionDepends = Annotated[Session, Depends(get_session)]

