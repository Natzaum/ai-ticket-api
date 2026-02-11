from app.db.models.ticket import TicketModel
from sqlalchemy.orm import Session
from sqlalchemy.sql import func


class TicketRepository:
    def save(self, db: Session, ticket: TicketModel):
        db.add(ticket)

        return ticket

    def list_all(self, db: Session):
        return db.query(TicketModel).filter(TicketModel.deleted_at.is_(None)).all()

    def list_by_id(self, db: Session, ticket_id: int):
        return (
            db.query(TicketModel)
            .filter(
                TicketModel.id == ticket_id,
                TicketModel.deleted_at.is_(None),
            )
            .first()
        )

    def update(
        self,
        ticket: TicketModel,
        category: str,
        priority: str,
        confidence: float,
    ) -> TicketModel:
        ticket.category = category
        ticket.priority = priority
        ticket.confidence = confidence

        return ticket

    def soft_delete(self, ticket: TicketModel) -> TicketModel:
        ticket.deleted_at = func.now()

        return ticket


ticket_repository = TicketRepository()
