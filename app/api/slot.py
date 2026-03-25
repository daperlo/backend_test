from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from datetime import datetime, timedelta
from app.db.session import get_db
from app.models.room import Room
from app.models.slot import Slot
from app.auth.dependencies import get_current_user

router = APIRouter()


@router.post("/rooms/{room_id}/generate-slots")
def generate_slots(
    room_id: str,
    interval_minutes: int = 30,
    db: Session = Depends(get_db),
    user=Depends(get_current_user)
):
    if user["role"] != "admin":
        raise HTTPException(status_code=403, detail="Forbidden")

    room = db.query(Room).filter(Room.id == room_id).first()
    if not room:
        raise HTTPException(status_code=404, detail="Room not found")

    if interval_minutes <= 0 or interval_minutes > 240:
        raise HTTPException(status_code=400, detail="Invalid interval")

    now = datetime.utcnow()
    end_period = now + timedelta(days=7)

    created = 0

    current = now.replace(second=0, microsecond=0)

    while current < end_period:
        slot_end = current + timedelta(minutes=interval_minutes)

        exists = db.query(Slot).filter(
            Slot.room_id == room.id,
            Slot.start_time == current
        ).first()

        if not exists:
            slot = Slot(
                room_id=room.id,
                start_time=current,
                end_time=slot_end,
                is_booked=False
            )
            db.add(slot)
            created += 1

        current = slot_end

    db.commit()

    return {
        "room": room.name,
        "created_slots": created,
        "interval": interval_minutes,
        "days": 7
    }