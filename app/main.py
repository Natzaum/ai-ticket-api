from fastapi import FastAPI
from schemas import TicketRequest, TicketResponse
from services.ml_service import ml_service

app = FastAPI()

@app.get("/")
def read_root():
  return {"API": "Alive"}

@app.post("/tickets/classify", response_model=TicketResponse)
def classify(ticket: TicketRequest):
  result = ml_service.predict(ticket.description)
  
  return TicketResponse(
    category=result["category"],
    priority=result["priority"],
    confidence=result["confidence"]
  )