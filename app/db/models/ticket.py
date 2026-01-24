from base import BaseModel
from sqlalchemy import String, Float, DateTime
from sqlalchemy.orm import Mapped, mapped_column


class TicketModel(BaseModel):
    __tablename__ = "tickets"

    id: Mapped[int] = mapped_column(primary_key=True)
    category: Mapped[str] = mapped_column(String(30))
    priority: Mapped[str] = mapped_column(String(30))
    confidence: Mapped[float] = mapped_column(Float)
    created_at: Mapped = mapped_column(DateTime(timezone=True))
