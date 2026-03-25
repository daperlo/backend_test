from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.models.slot import Slot
from app.models.booking import Booking
from app.models.room import Room

router = APIRouter()


@router.post("/booking")
def create_booking(data: dict, db: Session = Depends(get_db)):
    slot_id = data["slot_id"]
    user_id = data["user_id"]
    people_count = data["people_count"]

    slot = db.query(Slot).filter(Slot.id == slot_id).first()
    if not slot:
        raise HTTPException(status_code=404, detail="Slot not found")

    room = db.query(Room).filter(Room.id == slot.room_id).first()

    if people_count > room.capacity:
        raise HTTPException(status_code=400, detail="Too many people")


    existing_booking = db.query(Booking).filter(Booking.slot_id == slot_id).first()
    if existing_booking:
        raise HTTPException(status_code=400, detail="Slot already booked")


    user_bookings = (
        db.query(Booking)
        .join(Slot, Booking.slot_id == Slot.id)
        .filter(Booking.user_id == user_id)
        .all()
    )

    for b in user_bookings:
        booked_slot = db.query(Slot).filter(Slot.id == b.slot_id).first()

        if not (
            slot.end_time <= booked_slot.start_time
            or slot.start_time >= booked_slot.end_time
        ):
            raise HTTPException(status_code=400, detail="User already booked this time")

    booking = Booking(
        slot_id=slot_id,
        user_id=user_id,
        people_count=people_count
    )

    db.add(booking)
    db.commit()
    db.refresh(booking)

    return {
        "id": booking.id,
        "slot_id": booking.slot_id,
        "user_id": booking.user_id,
        "people_count": booking.people_count
    }