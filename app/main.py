from fastapi import FastAPI
from app.api.rooms import router as rooms_router
from app.auth.router import router as auth_router
from app.api.booking import router as Booking_router
from app.api import slot

app = FastAPI()
app.include_router(rooms_router)
app.include_router(auth_router)
app.include_router(Booking_router)
app.include_router(slot.router)