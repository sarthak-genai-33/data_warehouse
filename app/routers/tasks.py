from fastapi import APIRouter
from app.services.task_manager import list_tasks, cancel_task

router = APIRouter()

@router.get("/tasks")
async def get_tasks():
    return list_tasks()

@router.post("/tasks/cancel")
async def cancel_tasks(task_id: str):
    return cancel_task(task_id)
