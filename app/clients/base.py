from abc import ABC, abstractmethod
from typing import Any, Dict, List

class BlockchainClient(ABC):
    """Interface for blockchain network clients."""

    @abstractmethod
    async def get_node_info(self) -> Dict[str, Any]:
        """Fetch general information about the blockchain node."""
        pass

class MarketClient(ABC):
    """Interface for cryptocurrency market clients."""

    @abstractmethod
    async def get_top_prices(self) -> List[Dict[str, Any]]:
        """Fetch the top cryptocurrency prices from the market."""
        pass
