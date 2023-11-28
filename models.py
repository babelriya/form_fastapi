# from sqlalchemy import String, Boolean, Integer, Column

# from database import Base

# class details(Base):
#     __tablename__ = "details"

#     BU = Column[String]
#     App = Column[String]
#     CPU = Column[Integer]
#     Memory = Column[Integer]

from pydantic import BaseModel
from typing import List
from datetime import date
class Detail(BaseModel):
   BU: str
   App: str
   CPU: int
   Memory: int
   storage: int
   environment: str
   capacity : date
   cycleid: str

