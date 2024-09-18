from pydantic import BaseModel
from datetime import datetime

class CustomerBase(BaseModel):
    name: str
    email: str

class CustomerCreate(CustomerBase):
    pass

class Customer(CustomerBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True

class CampaignBase(BaseModel):
    name: str
    status: str

class CampaignCreate(CampaignBase):
    pass

class Campaign(CampaignBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True
