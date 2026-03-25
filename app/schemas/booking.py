
from pydantic import BaseModel
from uuid import UUID

class BookingCreate(BaseModel):
    slot_id: UUID
    people_count: int


class BookingResponse(BaseModel):
    id: UUID
    slot_id: UUID
    user_id: UUID
    people_count: int

    class Config:
        from_attributes = True