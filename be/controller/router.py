from fastapi import APIRouter
from controller import inventory

router = APIRouter()

router.include_router(inventory.router, tags=["Inventory"], prefix="/v1/inventory")
