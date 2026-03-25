from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.models.room import Room

router = APIRouter()


@router.post("/rooms")
def create_room(data: dict, db: Session = Depends(get_db)):
    room = Room(name=data["name"], capacity=data["capacity"])
    db.add(room)
    db.commit()
    db.refresh(room)

    return {
        "id": room.id,
        "name": room.name,
        "capacity": room.capacity
    }