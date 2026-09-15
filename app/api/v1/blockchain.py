from fastapi import APIRouter, Depends
from app.api.deps import get_blockchain_service
from app.services.blockchain_service import BlockchainService
from app.schemas.blockchain import BlockchainStatusResponse

router = APIRouter()

@router.get("/status", response_model=BlockchainStatusResponse)
async def get_blockchain_status(service: BlockchainService = Depends(get_blockchain_service)):
    """Retrieve the status of the blockchain network."""
    return await service.get_status()
