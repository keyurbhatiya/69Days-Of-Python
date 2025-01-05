from pydantic import BaseModel

class ItemBase(BaseModel):
    name: str
    description: str
    price: int
    available: int

class ItemCreate(ItemBase):
    pass

class ItemUpdate(ItemBase):
    pass

class Item(ItemBase):
    id: int

    class Config:
        orm_mode = True
