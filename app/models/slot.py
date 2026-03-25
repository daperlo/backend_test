from sqlalchemy import Column, Integer, DateTime, ForeignKey
from app.db.base import Base


class Slot(Base):
    __tablename__ = "slots"

    id = Column(Integer, primary_key=True, index=True)
    room_id = Column(Integer, ForeignKey("rooms.id"))
    start_time = Column(DateTime)
    end_time = Column(DateTime)