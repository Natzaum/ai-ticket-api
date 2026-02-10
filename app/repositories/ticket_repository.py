from app.db.models.ticket import TicketModel
from sqlalchemy.orm import Session


class TicketRepository:
    def save(self, db: Session, ticket: TicketModel):
        db.add(ticket)
        return ticket

    def list_all(self, db: Session):
        return db.query(TicketModel).all()

    def list_by_id(self, db: Session, ticket_id: int):
        return db.query(TicketModel).get(ticket_id)


ticket_repository = TicketRepository()
