from pydantic import BaseModel
from uuid import UUID
from typing import Optional


class RoomCreate(BaseModel):
    name: str
    description: Optional[str] = None
    capacity: Optional[int] = None


class RoomResponse(BaseModel):
    id: UUID
    name: str
    description: Optional[str]
    capacity: Optional[int]

    class Config:
        from_attributes = True