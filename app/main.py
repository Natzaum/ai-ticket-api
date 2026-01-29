from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError

from app.api.v1.routes.tickets import router as ticket_router
from app.api.v1.routes.health import router as health_router
from app.core.handlers import validation_exception_handler

app = FastAPI(title="AI Ticket Classifier API")

app.add_exception_handler(RequestValidationError, validation_exception_handler)  # type: ignore

app.include_router(health_router, prefix="/api/v1")
app.include_router(ticket_router, prefix="/api/v1")
