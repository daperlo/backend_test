from fastapi import FastAPI
from app.db.base import Base
from app.db.session import engine
from app.api.booking import router as Booking_router
import app.models.booking

app = FastAPI()

Base.metadata.create_all(bind=engine)

from app.api.rooms import router as rooms_router
from app.api.slot import router as slots_router

app.include_router(rooms_router)
app.include_router(slots_router)
app.include_router(Booking_router)