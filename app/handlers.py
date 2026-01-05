from fastapi import Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse


async def validation_exception_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=422,
        content={
            "error": "Validation Error",
            "message": "Please check your input",
            "status_code": 422,
        },
    )
