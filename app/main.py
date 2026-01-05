from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from schemas import TicketRequest, TicketResponse
from services.ml_service import ml_service
from handlers import validation_exception_handler

app = FastAPI(title="AI Ticket Classifier API")

app.add_exception_handler(RequestValidationError, validation_exception_handler)


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