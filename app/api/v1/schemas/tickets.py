from typing import Literal
from datetime import datetime
from pydantic import BaseModel


class TicketRequest(BaseModel):
    description: str


class TicketOut(BaseModel):
    id: int
    description: str
    category: Literal["billing", "technical", "account", "feature request", "other"]
    priority: Literal["low", "medium", "high"]
    confidence: float
    created_at: datetime

    class Config:
        from_attributes = True


class TicketCreateResponse(TicketOut):
    pass


class TicketListResponse(TicketOut):
    pass


class TicketDetailResponse(TicketOut):
    pass
