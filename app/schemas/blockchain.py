from pydantic import BaseModel
from typing import Any, Dict

class BlockchainStatusResponse(BaseModel):
    """Schema for the blockchain status response."""
    data: Dict[str, Any]
