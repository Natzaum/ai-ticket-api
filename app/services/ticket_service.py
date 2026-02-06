from sqlalchemy.orm import Session
from app.db.models.ticket import TicketModel
from app.services.ticket_classifier import ticket_classifier
from app.repositories.ticket_repository import ticket_repository
from app.api.v1.schemas.tickets import TicketRequest, TicketCreateResponse


class TicketService:
    def create_and_classify(
        self, db: Session, ticket: TicketRequest
    ) -> TicketCreateResponse:
        result = ticket_classifier.predict(ticket.description)

        ticket_model = TicketModel(
            description=ticket.description,
            category=result["category"],
            priority=result["priority"],
            confidence=result["confidence"],
        )
        ticket_repository.save(db, ticket_model)

        return TicketCreateResponse(
            description=ticket_model.description,
            category=ticket_model.category,  # type: ignore
            priority=ticket_model.priority,  # type: ignore
            confidence=ticket_model.confidence,
        )

    def list_all(self, db: Session):
        return ticket_repository.list_all(db)


ticket_service = TicketService()
