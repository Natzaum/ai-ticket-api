from schemas import TicketResponse

def classify_ticket_mock(description: str) -> TicketResponse:
  return TicketResponse(
    category="technical",
    priority="high",
    confidence=0.87
  )