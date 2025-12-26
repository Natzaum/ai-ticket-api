from schemas import TicketResponse

def classify_ticket_mock(description: str) -> TicketResponse:
  return TicketResponse(
    category="Technical",
    priority="high",
    confidence=0.87
  )