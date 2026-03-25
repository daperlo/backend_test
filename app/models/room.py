from sqlalchemy import Column, Integer, String
from app.db.base import Base


class Room(Base):
    tablename = "rooms"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    capacity = Column(Integer)