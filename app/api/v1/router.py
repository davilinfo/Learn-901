from fastapi import APIRouter
from app.api.v1 import status, blockchain, market

api_router = APIRouter()

# Base API status
api_router.include_router(status.router)

# Specialized endpoints with prefixes
api_router.include_router(blockchain.router, prefix="/blockchain", tags=["Blockchain"])
api_router.include_router(market.router, prefix="/market", tags=["Market"])
