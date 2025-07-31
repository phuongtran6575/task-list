from fastapi import FastAPI
from controller.task_controller import router as task_router
from controller.auth_controller import router as auth_router

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Task Project"}

app.include_router(task_router, prefix="/task", tags=["task"])
app.include_router(auth_router, prefix="/auth", tags=["auth"])
