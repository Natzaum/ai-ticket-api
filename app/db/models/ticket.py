from datetime import datetime
from app.db.models.base import BaseModel
from sqlalchemy import String, Float, DateTime
from sqlalchemy.orm import Mapped, mapped_column
from app.api.v1.schemas.tickets import TicketResponse


class TicketModel(BaseModel):
    __tablename__ = "tickets"

    id: Mapped[int] = mapped_column(primary_key=True)
    category: Mapped[str] = mapped_column(String(30))
    priority: Mapped[str] = mapped_column(String(30))
    confidence: Mapped[float] = mapped_column(Float)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True))


tickets_db: list[TicketResponse] = []
