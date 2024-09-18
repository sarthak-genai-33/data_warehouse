from fastapi import APIRouter, BackgroundTasks, HTTPException
from app.services.sync_service import sync_data

router = APIRouter()

@router.get("/sync/{source}")
async def trigger_sync(source: str, background_tasks: BackgroundTasks):
    if source not in ["crm", "marketing"]:
        raise HTTPException(status_code=400, detail="Invalid source")
    background_tasks.add_task(sync_data, source)
    return {"message": f"Sync triggered for {source}"}
