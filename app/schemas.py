from pydantic import BaseModel

class TicketRequest(BaseModel):
  description: str
  
class TicketResponse(BaseModel):
  category: str
  priority: str
  confidence: float
