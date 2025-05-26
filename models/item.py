from sqlalchemy import Column, Integer, String
from db.session import Base

class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    description = Column(String)
    equipment = Column(String)  # ✅ Now this matches the Pydantic schema

