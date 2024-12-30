from fastapi import APIRouter, Depends
from core.schemas.inventory import Inventory
from repositories.interface.IInventoryRepository import IInventoryRepository
from repositories.repositories.InventoryRepository import InventoryRepository
from services.interface.IInventoryService import IInventoryService
from services.services.IventoryService import InventoryService
from database.database import get_db

router = APIRouter()

def get_repository(db_session = Depends(get_db)) -> IInventoryRepository:
    return InventoryRepository(db_session)

def get_inventory_service(repository: IInventoryRepository = Depends(get_repository)) -> IInventoryService:
    return InventoryService(repository)

@router.post("/")
def insert_inventory(inventories: list[Inventory], service: IInventoryService = Depends(get_inventory_service)):
  result = service.insert_inventory(inventories)
  return result