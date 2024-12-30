from core.schemas.inventory import Inventory
from repositories.interface.IInventoryRepository import IInventoryRepository
from services.interface.IInventoryService import IInventoryService

class InventoryService(IInventoryService):
  def __init__(self, repository: IInventoryRepository):
    self.repository = repository

  def insert_inventory(self, inventories: list[Inventory]):
    duplicates = self.repository.insert_inventory(inventories)

    if duplicates:
      return {
        "type": "error",
        "message": f"Bị trùng barcode: {', '.join(map(str, duplicates))}"
      }

    return {
      "type": "success",
      "message": "Thêm thành công"
    }