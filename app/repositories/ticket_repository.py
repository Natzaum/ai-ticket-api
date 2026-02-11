from app.db.models.ticket import TicketModel
from sqlalchemy.orm import Session


class TicketRepository:
    def save(self, db: Session, ticket: TicketModel):
        db.add(ticket)
        db.commit()
        db.refresh(ticket)
        return ticket

    def list_all(self, db: Session):
        return db.query(TicketModel).all()

    def list_by_id(self, db: Session, ticket_id: int):
        return db.query(TicketModel).get(ticket_id)

    def update(
        self,
        db: Session,
        ticket: TicketModel,
        category: str,
        priority: str,
        confidence: float,
    ) -> TicketModel:
        ticket.category = category
        ticket.priority = priority
        ticket.confidence = confidence

        db.commit()
        db.refresh(ticket)

        return ticket


ticket_repository = TicketRepository()
