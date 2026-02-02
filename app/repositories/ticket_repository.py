from app.db.models.ticket import TicketModel
from sqlalchemy.orm import Session


class TicketRepository:
    def save(self, db: Session, ticket: TicketModel):
        db.add(ticket)
        db.commit()
        db.refresh(ticket)
        return ticket

    def list_all(self, db: Session):
        return db


ticket_repository = TicketRepository()
