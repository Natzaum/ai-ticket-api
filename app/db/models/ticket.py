from datetime import datetime
from sqlalchemy.sql import func
from app.db.base import BaseModel
from sqlalchemy import String, Float, DateTime
from sqlalchemy.orm import Mapped, mapped_column


class TicketModel(BaseModel):
    __tablename__ = "tickets"

    id: Mapped[int] = mapped_column(primary_key=True)
    category: Mapped[str] = mapped_column(String(30), nullable=False)
    priority: Mapped[str] = mapped_column(String(30), nullable=False)
    confidence: Mapped[float] = mapped_column(Float, nullable=False)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now(), nullable=False
    )
