from typing import List
from fastapi import Depends, APIRouter, HTTPException
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.api.v1.schemas.tickets import (
    TicketRequest,
    TicketCreateResponse,
    TicketDetailResponse,
    TicketListResponse,
)
from app.services.ticket_service import ticket_service

router = APIRouter(prefix="/tickets", tags=["Tickets"])


@router.post("/classify", response_model=TicketCreateResponse)
def classify_ticket(ticket: TicketRequest, db: Session = Depends(get_db)):
    return ticket_service.create_and_classify(db, ticket)


@router.get("/", response_model=List[TicketListResponse])
def get_all_tickets(db: Session = Depends(get_db)):
    return ticket_service.list_all(db)


@router.get("/{ticket_id}", response_model=TicketDetailResponse)
def get_ticket_by_id(ticket_id: int, db: Session = Depends(get_db)):
    ticket = ticket_service.get_by_id(db, ticket_id)
    if ticket is None:
        raise HTTPException(status_code=404, detail="Ticket not found")

    return ticket
