from fastapi import APIRouter
from database.sqlite_database_config import SessionDepends
from models.task_model import Task
from sqlmodel import select

router = APIRouter()


@router.get("/task")
async def get_task_by_id(id: int, session: SessionDepends):
    statment = select(Task).where(Task.id == id)
    task_result = session.exec(statment).first()
    return task_result

@router.get("/tasks")
async def get_all_task(session: SessionDepends):
    statement = select(Task)
    tasks_result = session.exec(statement).all()
    return tasks_result

@router.post("/tasks")
async def create_task(task: Task,session: SessionDepends):
    session.add(task)
    session.commit()
    session.refresh(task)
    return task

@router.delete("/task")
async def delete_task(id: int, session: SessionDepends):
    statement = select(Task).where(Task.id == id)
    task_result = session.exec(statement).first()
    session.delete(task_result)
    session.commit()
    
    return {"Ok"}