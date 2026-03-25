from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from datetime import datetime, timedelta

from app.db.session import get_db
from app.models.slot import Slot
from app.models.room import Room

router = APIRouter(prefix="/rooms", tags=["slots"])


@router.get("/{room_id}/slots")
def get_slots(room_id: int, db: Session = Depends(get_db)):
    slots = db.query(Slot).filter(Slot.room_id == room_id).all()

    return {
        "slots": [
            {
                "id": s.id,
                "room_id": s.room_id,
                "start_time": s.start_time,
                "end_time": s.end_time
            }
            for s in slots
        ]
    }


@router.post("/{room_id}/generate-slots")
def generate_slots(
    room_id: int,
    interval_minutes: int = Query(...),
    db: Session = Depends(get_db)
):
    room = db.query(Room).filter(Room.id == room_id).first()

    if not room:
        return {"created_slots": 0}

    start = datetime(2024, 1, 1, 10, 0)
    end = datetime(2024, 1, 1, 18, 0)

    existing = db.query(Slot).filter(Slot.room_id == room_id).all()
    existing_set = {(s.start_time, s.end_time) for s in existing}

    created = 0
    current = start

    while current + timedelta(minutes=interval_minutes) <= end:
        slot = (current, current + timedelta(minutes=interval_minutes))

        if slot not in existing_set:
            db.add(Slot(
                room_id=room_id,
                start_time=slot[0],
                end_time=slot[1]
            ))
            created += 1

        current += timedelta(minutes=interval_minutes)

    db.commit()

    return {"created_slots": created}