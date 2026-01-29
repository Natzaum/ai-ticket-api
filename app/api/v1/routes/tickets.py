from fastapi import APIRouter
from app.api.v1.schemas.tickets import TicketRequest
from app.services.ticket_service import ticket_service

router = APIRouter(prefix="/tickets", tags=["Tickets"])


@router.post("/classify")
def classify(ticket: TicketRequest):
    return ticket_service.create_and_classify(ticket)
