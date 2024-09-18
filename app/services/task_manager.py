import asyncio

tasks = {}

def list_tasks():
    return tasks

def cancel_task(task_id):
    if task_id in tasks:
        tasks[task_id].cancel()
        del tasks[task_id]
        return {"message": f"Task {task_id} cancelled"}
    return {"message": f"Task {task_id} not found"}

def add_task(task_id, task):
    tasks[task_id] = task
