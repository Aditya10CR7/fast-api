from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import List

from db.session import get_db
from models.item import Item
from schemas.item import ItemCreate, ItemResponse

router = APIRouter(prefix="/items", tags=["Items"])

# POST /items
@router.post("/", response_model=ItemResponse)
def create_item(item: ItemCreate, db: Session = Depends(get_db)):
    db_item = Item(**item.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

# GET /items/{id}
@router.get("/{item_id}", response_model=ItemResponse)
def get_item(item_id: int, db: Session = Depends(get_db)):
    item = db.query(Item).filter(Item.id == item_id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item

# GET /items?page=1&limit=10
@router.get("/", response_model=List[ItemResponse])
def list_items(
    page: int = Query(1, ge=1),
    limit: int = Query(10, ge=1),
    db: Session = Depends(get_db)
):
    offset = (page - 1) * limit
    items = db.query(Item).offset(offset).limit(limit).all()
    return items
