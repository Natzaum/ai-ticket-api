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
            return ticket_repository.save(db, ticket_model)

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

        return ticket_repository.update(
            db,
            ticket,
            category=data.category,
            priority=data.priority,
            confidence=data.confidence,
        )


ticket_service = TicketService()
