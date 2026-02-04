from typing import List
from fastapi import Depends
from fastapi import APIRouter
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.api.v1.schemas.tickets import TicketRequest, TicketResponse
from app.services.ticket_service import ticket_service

router = APIRouter(prefix="/tickets", tags=["Tickets"])


@router.post("/classify")
def classify_ticket(ticket: TicketRequest, db: Session = Depends(get_db)):
    return ticket_service.create_and_classify(db, ticket)


@router.get("/", response_model=List[TicketResponse])
def get_all_tickets(db: Session = Depends(get_db)):
    return ticket_service.list_all(db)
