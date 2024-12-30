from pydantic import BaseModel
from datetime import datetime

class Inventory(BaseModel):
  code: str
  datetime: datetime