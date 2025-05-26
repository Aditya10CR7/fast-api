from pydantic import BaseModel

class ItemCreate(BaseModel):
    name: str
    description: str
    equipment: str  # 👈 this is in the schema

class ItemResponse(ItemCreate):
    id: int

    class Config:
        orm_mode = True
