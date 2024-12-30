from abc import ABC, abstractmethod
from core.schemas.inventory import Inventory

class IInventoryRepository(ABC):
  @abstractmethod
  def insert_inventory(self, inventories: list[Inventory]) -> list[str]:
    pass