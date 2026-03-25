from fastapi import FastAPI

from app.api.rooms import router as room_router
from app.api.slot import router as slot_router

app = FastAPI()

app.include_router(room_router)
app.include_router(slot_router)