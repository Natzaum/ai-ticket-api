from typing import Literal
from pydantic import BaseModel, field_validator


class TicketRequest(BaseModel):
    description: str

    @field_validator("description")
    @classmethod
    def validate_description(cls, value):
        value = value.strip()

        if not value:
            raise ValueError("Description cannot be empty or contain only whitespace")

        if len(value) < 10:
            raise ValueError(
                f"Description is too short ({len(value)} characters). Minimum is 10 characters."
            )

        if len(value) > 1500:
            raise ValueError(
                f"Description is too long ({len(value)} characters). Maximum is 1500 characters."
            )

        return value


class TicketResponse(BaseModel):
    category: Literal["billing", "technical", "account", "feature request", "other"]
    priority: Literal["low", "medium", "high"]
    confidence: float


class ErrorResponse(BaseModel):
    error: str
    detail: str
    status_code: int
