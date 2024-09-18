import aiohttp
import asyncio
from app.database import SessionLocal
from app.models import Customer, Campaign
from app.schemas import CustomerCreate, CampaignCreate

API_KEY = "sarthak123kanungo@gmail.com"

async def fetch_data(url, params):
    async with aiohttp.ClientSession() as session:
        async with session.get(url, params=params, headers={"X-API-Key": API_KEY}) as response:
            return await response.json()

async def sync_data(source):
    db = SessionLocal()
    if source == "crm":
        url = "https://challenge.berrydev.ai/api/crm/customers"
        params = {"limit": 100, "offset": 0}
        data = await fetch_data(url, params)
        for customer in data["customers"]:
            customer_data = CustomerCreate(**customer)
            db_customer = Customer(**customer_data.dict())
            db.add(db_customer)
    elif source == "marketing":
        url = "https://challenge.berrydev.ai/api/marketing/campaigns"
        params = {}
        data = await fetch_data(url, params)
        for campaign in data["campaigns"]:
            campaign_data = CampaignCreate(**campaign)
            db_campaign = Campaign(**campaign_data.dict())
            db.add(db_campaign)
    db.commit()
    db.close()
