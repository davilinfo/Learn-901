from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from app.api.v1.router import api_router
from app.core.exceptions import AppException, ExternalAPIError
from app.core.config import settings

app = FastAPI(
    title=settings.APP_NAME,
    description="A SOLID-compliant API proxy for Blockchain and Market data.",
    version="1.0.0"
)

# Global Exception Handler
@app.exception_handler(AppException)
async def app_exception_handler(_request: Request, exc: AppException):
    """Handles application-specific exceptions and returns consistent JSON responses."""
    status_code = 500

    if isinstance(exc, ExternalAPIError):
        status_code = 502 # Bad Gateway

    return JSONResponse(
        status_code=status_code,
        content={
            "error": exc.__class__.__name__,
            "message": exc.message
        }
    )

# Include the API router
app.include_router(api_router, prefix="/api/v1")

@app.get("/")
async def root():
    """Root endpoint providing information about the API."""
    return {
        "message": "Welcome to the Blockchain & Market Status API",
        "docs": "/docs"
    }
