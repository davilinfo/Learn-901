import httpx
from typing import Any, Dict, List
from app.clients.base import MarketClient
from app.core.config import settings
from app.core.exceptions import ExternalAPIError

class CoinGeckoClient(MarketClient):
    """CoinGecko implementation of the MarketClient interface."""

    def __init__(self):
        self.url = settings.COINGECKO_API_URL

    async def get_top_prices(self) -> List[Dict[str, Any]]:
        async with httpx.AsyncClient() as client:
            try:
                response = await client.get(self.url, timeout=10.0)
                response.raise_for_status()
                return response.json()
            except httpx.HTTPStatusError as e:
                raise ExternalAPIError(f"CoinGecko API returned an error: {e.response.status_code}") from e
            except httpx.RequestError as e:
                raise ExternalAPIError(f"Failed to connect to CoinGecko API: {str(e)}") from e
