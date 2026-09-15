import httpx
from typing import Any, Dict
from app.clients.base import BlockchainClient
from app.core.config import settings
from app.core.exceptions import ExternalAPIError

class LiskClient(BlockchainClient):
    """Lisk Blockchain implementation of the BlockchainClient interface."""

    def __init__(self):
        self.url = settings.LISK_API_URL

    async def get_node_info(self) -> Dict[str, Any]:
        async with httpx.AsyncClient() as client:
            try:
                response = await client.get(self.url, timeout=10.0)
                response.raise_for_status()
                return response.json()
            except httpx.HTTPStatusError as e:
                raise ExternalAPIError(f"Lisk API returned an error: {e.response.status_code}") from e
            except httpx.RequestError as e:
                raise ExternalAPIError(f"Failed to connect to Lisk API: {str(e)}") from e
