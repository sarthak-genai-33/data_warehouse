from fastapi import FastAPI
from app.database import engine, Base
from app.routers import webhook, data, sync, tasks

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(webhook.router)
app.include_router(data.router)
app.include_router(sync.router)
app.include_router(tasks.router)
