from typing import Annotated
from sqlmodel import SQLModel, create_engine, Depends, Session

engine = create_engine()
SQLModel.metadata.create_all(engine)
def get_session():
    with Session(engine) as session:
        yield session

SessionDepends = Annotated[Session, Depends(get_session)]

