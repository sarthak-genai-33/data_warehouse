from fastapi import APIRouter, HTTPException
from app.schemas import CustomerCreate, CampaignCreate
from app.database import SessionLocal
from app.models import Customer, Campaign

router = APIRouter()

@router.post("/webhook")
async def receive_webhook(data: dict):
    db = SessionLocal()
    try:
        if 'customer' in data:
            customer_data = CustomerCreate(**data['customer'])
            db_customer = Customer(**customer_data.dict())
            db.add(db_customer)
        elif 'campaign' in data:
            campaign_data = CampaignCreate(**data['campaign'])
            db_campaign = Campaign(**campaign_data.dict())
            db.add(db_campaign)
        db.commit()
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=400, detail=str(e))
    finally:
        db.close()
    return {"message": "Data received successfully"}
