from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from schemas import TicketRequest, TicketResponse
from services.ml_service import ml_service
from handlers import validation_exception_handler

app = FastAPI(title="AI Ticket Classifier API")

app.add_exception_handler(RequestValidationError, validation_exception_handler)  # type: ignore

tickets_db: list[TicketResponse] = []


@app.get("/")
async def read_root():
    return {"API": "Alive"}


@app.post("/tickets/classify/", response_model=TicketResponse)
async def classify(ticket: TicketRequest):
    result = ml_service.predict(ticket.description)

    ticket_response = TicketResponse(
        category=result["category"],
        priority=result["priority"],
        confidence=result["confidence"],
    )

    tickets_db.append(ticket_response)
    return ticket_response


@app.get("/tickets/")
async def get_all_tickets():
    return tickets_db
