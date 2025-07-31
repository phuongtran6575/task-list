from fastapi import APIRouter
from database.sqlite_database_config import SessionDepends
from models.task_model import Task
from sqlmodel import select

router = APIRouter()

@router.get("/task/{task_id}")
async def get_task_by_id(task_id: int, session: SessionDepends ):
    statement = session.select(Task).where(Task.id == task_id)
    task_result = session.exec(statement).first()
    return task_result

@router.get("/tasks")
async def get_all_tasks(session: SessionDepends):
    statement = select(Task)
    tasks_result = session.exec(statement).all()
    return

@router.post("/task")
async def create_task(task: Task, session: SessionDepends):
    session.add(task)
    session.commit()
    session.refresh(task)
    return task

@router.put("/task")
async def update_task(task: Task, session: SessionDepends):
    statement = session.select(Task).where(Task.id == task.id)
    task_result = session.exec(statement).first()
    task_result = task
    session.commit()
    session.refresh(task_result)
    return task_result

@router.delete("/task")
async def delete_task(task_id: int, session: SessionDepends):
    statement = session.select(Task).where(Task.id == task_id)
    task_result = session.excec(statement).first()
    session.delete()
    session.commit()
    session.refresh(task_result)
    return task_result
    