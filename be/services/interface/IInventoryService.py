from abc import ABC, abstractmethod
from core.schemas.inventory import Inventory

class IInventoryService(ABC):
  @abstractmethod
  def insert_inventory(self, inventories: list[Inventory]):
    pass