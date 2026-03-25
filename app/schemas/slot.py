from pydantic import BaseModel
from datetime import datetime
import uuid


class SlotResponse(BaseModel):
    id: uuid.UUID
    room_id: uuid.UUID
    start_time: datetime
    end_time: datetime
    is_booked: bool

    class Config:
        from_attributes = True