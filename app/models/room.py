import uuid
from typing import TYPE_CHECKING

from sqlalchemy import String, Integer, Column
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base import Base

if TYPE_CHECKING:
    from app.models.slot import Slot


class Room(Base):
    __tablename__ = "rooms"

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)

    name: Mapped[str] = mapped_column(String, unique=True, nullable=False)
    capacity: Mapped[int] = mapped_column(Integer, nullable=False)
    description = Column(String, nullable=True)

    slots: Mapped[list["Slot"]] = relationship(
        "Slot",
        back_populates="room",
        cascade="all, delete-orphan"
    )