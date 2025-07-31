from sqlmodel import SQLModel, Field

class TaskBase(SQLModel):
    name: str

class Task(TaskBase, table=True):
    id: int = Field(default=None, primary_key=True)