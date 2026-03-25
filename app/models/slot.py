import uuid
from datetime import datetime
from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey, DateTime, Boolean, Index
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base import Base

if TYPE_CHECKING:
    from app.models.room import Room
    from app.models.booking import Booking


class Slot(Base):
    __tablename__ = "slots"

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)

    room_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("rooms.id", ondelete="CASCADE"),
        index=True
    )

    start_time: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    end_time: Mapped[datetime] = mapped_column(DateTime, nullable=False)

    is_booked: Mapped[bool] = mapped_column(Boolean, default=False)

    # связи
    room: Mapped["Room"] = relationship("Room", back_populates="slots")

    booking: Mapped["Booking"] = relationship(
        "Booking",
        back_populates="slot",
        uselist=False,
        cascade="all, delete-orphan"
    )

    __table_args__ = (
        Index("ix_unique_slot", "room_id", "start_time", unique=True),
    )