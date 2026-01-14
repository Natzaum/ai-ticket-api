class TicketAPIException(Exception):
    def __init__(self, message: str, status_code: int = 500):
        self.message = message
        self.status_code = status_code
        super().__init__(self.message)


class TicketClassificationError(TicketAPIException):
    def __init__(self, message: str = "Failed to classify ticket"):
        super().__init__(message, status_code=500)
