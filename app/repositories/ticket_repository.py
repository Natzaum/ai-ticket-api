from app.db.models.ticket import tickets_db


class TicketRepository:
    def save(self, ticket):
        return tickets_db.append(ticket)

    def list_all(self):
        return tickets_db


ticket_repository = TicketRepository()
