from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.models.room import Room

router = APIRouter(prefix="/rooms", tags=["rooms"])


@router.post("")
def create_room(data: dict, db: Session = Depends(get_db)):
    room = Room(**data)
    db.add(room)
    db.commit()
    db.refresh(room)
    return room

from app.models.slot import Slot
@router.get("/{room_id}/slots")
def get_slots(room_id: int, db: Session = Depends(get_db)):
    slots = db.query(Slot).filter(Slot.room_id == room_id).all()

    return {
        "slots": [
            {
                "slot_id": s.id,
                "start_time": s.start_time,
                "end_time": s.end_time
            }
            for s in slots
        ]
    }