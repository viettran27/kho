from sqlalchemy.orm import Session
from core.schemas.inventory import Inventory
from core.model.inventory import InventoryModel
from repositories.interface.IInventoryRepository import IInventoryRepository

class InventoryRepository(IInventoryRepository):
  def __init__(self, db: Session):
    self.db = db

  def insert_inventory(self, inventories: list[Inventory]) -> list[str]:
    inventory_codes = {inventory.code for inventory in inventories}

    existing_inventories = self.db.query(InventoryModel).filter(InventoryModel.Carton_Barcode.in_(inventory_codes)).all()
    existing_inventory_codes = {inventory.Carton_Barcode for inventory in existing_inventories}

    duplicates = inventory_codes.intersection(existing_inventory_codes)
    inventories_to_insert = [InventoryModel(Carton_Barcode=inventory.code, Time_Stamp=inventory.datetime) for inventory in inventories if inventory.code not in existing_inventory_codes]

    if inventories_to_insert:
      self.db.add_all(inventories_to_insert)
      self.db.commit()

    return duplicates