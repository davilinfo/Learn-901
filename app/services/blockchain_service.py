from app.clients.base import BlockchainClient
from app.schemas.blockchain import BlockchainStatusResponse

class BlockchainService:
    """Business logic for blockchain operations."""

    def __init__(self, client: BlockchainClient):
        self.client = client

    async def get_status(self) -> BlockchainStatusResponse:
        """Fetch and format the blockchain status."""
        data = await self.client.get_node_info()
        return BlockchainStatusResponse(data=data)
