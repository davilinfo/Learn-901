from fastapi import APIRouter
from datetime import datetime
from typing import Dict

router = APIRouter()

@router.get("/status")
async def get_api_status() -> Dict[str, str]:
    """Health check endpoint."""
    return {
        "status": "online",
        "timestamp": datetime.utcnow().isoformat()
    }
