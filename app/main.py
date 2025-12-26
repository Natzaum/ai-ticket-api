from fastapi import FastAPI
from schemas import TicketRequest, TicketResponse
from services.classifier import classify_ticket_mock

app = FastAPI()

@app.get("/")
def read_root():
  return {"API": "Alive"}

@app.post("/tickets/classify", response_model=TicketResponse)
def classify_ticket(ticket: TicketRequest):
  return classify_ticket_mock(ticket.description)