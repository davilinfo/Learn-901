from typing import List
from app.clients.base import MarketClient
from app.schemas.market import MarketPricesResponse, CoinMarketData

class MarketService:
    """Business logic for market data operations."""

    def __init__(self, client: MarketClient):
        self.client = client

    async def get_top_market_prices(self) -> MarketPricesResponse:
        """Fetch and format the top cryptocurrency prices."""
        raw_coins = await self.client.get_top_prices()

        # Map raw data to Pydantic models
        coins = [
            CoinMarketData(
                id=coin.get("id"),
                symbol=coin.get("symbol"),
                name=coin.get("name"),
                current_price=coin.get("current_price"),
                market_cap=coin.get("market_cap"),
                market_cap_rank=coin.get("market_cap_rank")
            )
            for coin in raw_coins
        ]

        return MarketPricesResponse(coins=coins)
