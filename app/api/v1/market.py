from fastapi import APIRouter, Depends
from app.api.deps import get_market_service
from app.services.market_service import MarketService
from app.schemas.market import MarketPricesResponse

router = APIRouter()

@router.get("/prices", response_model=MarketPricesResponse)
async def get_market_prices(service: MarketService = Depends(get_market_service)):
    """Retrieve top cryptocurrency market prices."""
    return await service.get_top_market_prices()
