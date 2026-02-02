from sqlalchemy.orm import Session
from app.db.models.ticket import TicketModel
from app.services.ticket_classifier import ticket_classifier
from app.repositories.ticket_repository import ticket_repository
from app.api.v1.schemas.tickets import TicketRequest, TicketResponse


class TicketService:
    def create_and_classify(self, db: Session, ticket: TicketRequest) -> TicketResponse:
        result = ticket_classifier.predict(ticket.description)

        ticket_model = TicketModel(
            category=result["category"],
            priority=result["priority"],
            confidence=result["confidence"],
        )
        ticket_repository.save(db, ticket_model)

        return TicketResponse(
            category=ticket_model.category,  # type: ignore
            priority=ticket_model.priority,  # type: ignore
            confidence=ticket_model.confidence,
        )


ticket_service = TicketService()
