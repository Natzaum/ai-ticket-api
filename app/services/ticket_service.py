from sqlalchemy.orm import Session
from app.db.models.ticket import TicketModel
from app.services.ticket_classifier import ticket_classifier
from app.repositories.ticket_repository import ticket_repository
from app.api.v1.schemas.tickets import TicketRequest, TicketUpdateRequest


class TicketService:
    def create_and_classify(self, db: Session, ticket: TicketRequest) -> TicketModel:
        try:
            result = ticket_classifier.predict(ticket.description)

            ticket_model = TicketModel(
                description=ticket.description,
                category=result["category"],
                priority=result["priority"],
                confidence=result["confidence"],
            )

            ticket_repository.save(db, ticket_model)

            db.commit()
            db.refresh(ticket_model)

            return ticket_model

        except Exception:
            db.rollback()
            raise

    def list_all(self, db: Session):
        return ticket_repository.list_all(db)

    def get_by_id(self, db: Session, ticket_id: int):
        return ticket_repository.list_by_id(db, ticket_id)

    def update_ticket(self, db: Session, ticket_id: int, data: TicketUpdateRequest):
        ticket = ticket_repository.list_by_id(db, ticket_id)

        if ticket is None:
            return None

        ticket_model = ticket_repository.update(
            ticket,
            category=data.category,
            priority=data.priority,
            confidence=data.confidence,
        )

        db.commit()
        db.refresh(ticket)

        return ticket_model

    def delete_ticket(self, db: Session, ticket_id: int):
        ticket = ticket_repository.list_by_id(db, ticket_id)

        if ticket is None:
            return None

        deleted = ticket_repository.soft_delete(ticket)

        db.commit()
        db.refresh(ticket)

        return deleted


ticket_service = TicketService()
