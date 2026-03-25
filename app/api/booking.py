from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.models.slot import Slot
from app.db.session import get_db
from app.auth.dependencies import get_current_user
from app.models.booking import Booking
from app.models.room import Room
from app.schemas.booking import BookingCreate, BookingResponse

router = APIRouter()

@router.post("/bookings")
def create_booking(
    slot_id: str,
    people_count: int,
    db: Session = Depends(get_db),
    user=Depends(get_current_user)
):
    if user["role"] != "user":
        raise HTTPException(status_code=403)

    slot = db.query(Slot).filter(Slot.id == slot_id).first()

    if not slot:
        raise HTTPException(status_code=404, detail="Slot not found")

    if slot.is_booked:
        raise HTTPException(status_code=409, detail="Slot already booked")

    booking = Booking(
        slot_id=slot_id,
        user_id=user["user_id"],
        people_count=people_count
    )

    slot.is_booked = True

    db.add(booking)
    db.commit()
    db.refresh(booking)

    return booking