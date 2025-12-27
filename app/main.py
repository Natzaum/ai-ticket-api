from fastapi import FastAPI
from schemas import TicketRequest, TicketResponse
from services.classifier import classifier

app = FastAPI()

@app.get("/")
def read_root():
  return {"API": "Alive"}

@app.post("/tickets/classify", response_model=TicketResponse)
def classify(ticket: TicketRequest):
  return classifier.classify(ticket.description)