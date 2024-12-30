from sqlalchemy import Column, Integer, String, DateTime
from core.model.base import Base

class InventoryModel(Base):
    __tablename__ = "KIEM_KE"
    Carton_Barcode = Column(String(100), primary_key=True)
    Time_Stamp = Column(DateTime)
