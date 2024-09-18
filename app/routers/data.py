from fastapi import APIRouter, Query
from app.database import SessionLocal
from app.models import Customer, Campaign

router = APIRouter()

@router.get("/data")
async def get_data(offset: int = Query(0), limit: int = Query(10)):
    db = SessionLocal()
    customers = db.query(Customer).offset(offset).limit(limit).all()
    campaigns = db.query(Campaign).offset(offset).limit(limit).all()
    db.close()
    return {"customers": customers, "campaigns": campaigns}
