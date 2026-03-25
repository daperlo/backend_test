from sqlalchemy import Column, Integer, ForeignKey, String
from app.db.base import Base


class Booking(Base):
    __tablename__ = "bookings"

    id = Column(Integer, primary_key=True, index=True)
    slot_id = Column(Integer, ForeignKey("slots.id"), nullable=False)
    user_id = Column(String, nullable=False)
    people_count = Column(Integer, nullable=False)