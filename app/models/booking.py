import uuid
from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base import Base

if TYPE_CHECKING:
    from app.models.slot import Slot


class Booking(Base):
    __tablename__ = "bookings"

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)

    slot_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("slots.id", ondelete="CASCADE"),
        unique=True
    )

    user_id: Mapped[uuid.UUID] = mapped_column(nullable=False)

    people_count: Mapped[int] = mapped_column(Integer, nullable=False)

    # связь
    slot: Mapped["Slot"] = relationship("Slot", back_populates="booking")