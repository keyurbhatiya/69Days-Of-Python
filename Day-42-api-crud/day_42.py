################################## Day 42: 69 Days of Python #####################################

# API CRUD

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

# Define an in-memory database (a dictionary for simplicity)
fake_db = {}

# Define the Pydantic model for an item
class Item(BaseModel):
    id: int
    name: str
    description: str = None
    price: float

# CRUD Operations

# Create
@app.post("/items/", response_model=Item)
def create_item(item: Item):
    if item.id in fake_db:
        raise HTTPException(status_code=400, detail="Item with this ID already exists")
    fake_db[item.id] = item
    return item

# Read All
@app.get("/items/", response_model=List[Item])
def read_items():
    return list(fake_db.values())

# Read Single
@app.get("/items/{item_id}", response_model=Item)
def read_item(item_id: int):
    if item_id not in fake_db:
        raise HTTPException(status_code=404, detail="Item not found")
    return fake_db[item_id]

# Update
@app.put("/items/{item_id}", response_model=Item)
def update_item(item_id: int, updated_item: Item):
    if item_id not in fake_db:
        raise HTTPException(status_code=404, detail="Item not found")
    fake_db[item_id] = updated_item
    return updated_item

# Delete
@app.delete("/items/{item_id}", response_model=dict)
def delete_item(item_id: int):
    if item_id not in fake_db:
        raise HTTPException(status_code=404, detail="Item not found")
    del fake_db[item_id]
    return {"message": "Item deleted successfully"}

# Run the FastAPI application
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)