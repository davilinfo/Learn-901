from app.clients.blockchain_client import LiskClient
from app.clients.market_client import CoinGeckoClient
from app.services.blockchain_service import BlockchainService
from app.services.market_service import MarketService

def get_blockchain_service() -> BlockchainService:
    """Provides a BlockchainService instance with a LiskClient."""
    client = LiskClient()
    return BlockchainService(client)

def get_market_service() -> MarketService:
    """Provides a MarketService instance with a CoinGeckoClient."""
    client = CoinGeckoClient()
    return MarketService(client)
