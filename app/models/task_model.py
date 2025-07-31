from sqlmodel import SQLModel, Field

class TaskBase(SQLModel):
    name: str
    owner_id = Field(default=None, foreign_key="user.id")

class Task(TaskBase, table=True):
    int: id = Field(default=None, primary_key=True)