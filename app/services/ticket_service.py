from app.services.ticket_classifier import ticket_classifier
from app.repositories.ticket_repository import ticket_repository
from app.api.v1.schemas.tickets import TicketRequest, TicketResponse


class TicketService:
    def create_and_classify(self, ticket: TicketRequest) -> TicketResponse:
        result = ticket_classifier.predict(ticket.description)

        ticket_response = TicketResponse(
            category=result["category"],
            priority=result["priority"],
            confidence=result["confidence"],
        )
        ticket_repository.save(ticket_response)

        return ticket_response


ticket_service = TicketService()
