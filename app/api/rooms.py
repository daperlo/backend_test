from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.models.room import Room
from app.schemas.room import RoomCreate, RoomResponse
from app.auth.dependencies import get_current_user

router = APIRouter(prefix="/rooms", tags=["Rooms"])


@router.post("", response_model=RoomResponse)
def create_room(
    data: RoomCreate,
    db: Session = Depends(get_db),
    user=Depends(get_current_user)
):
    if user("role") != "admin":
        raise HTTPException(status_code=403, detail="Only admin can create rooms")

    room = Room(**data.model_dump())
    db.add(room)
    db.commit()
    db.refresh(room)

    return room


@router.get("", response_model=list[RoomResponse])
def get_rooms(
    db: Session = Depends(get_db),
    user=Depends(get_current_user)
):
    rooms = db.query(Room).all()
    return rooms   