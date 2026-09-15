from pydantic import BaseModel
from typing import List, Optional

class CoinMarketData(BaseModel):
    """Schema for individual coin market data."""
    id: str
    symbol: str
    name: str
    current_price: float
    market_cap: float
    market_cap_rank: int

class MarketPricesResponse(BaseModel):
    """Schema for the top market prices response."""
    coins: List[CoinMarketData]
