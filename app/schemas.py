from typing import Literal
from pydantic import BaseModel, Field

class TicketRequest(BaseModel):
  description: str = Field(..., min_length=10, max_length=1500)  
  
class TicketResponse(BaseModel):
  category: Literal["billing", "technical", "account", "feature request", "other"]
  priority: Literal["low", "medium", "high"]
  confidence: float