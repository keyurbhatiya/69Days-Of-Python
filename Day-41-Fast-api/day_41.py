################################## Day 40: 69 Days of Python #####################################

# FastAPI

# pip install fastapi

# FastAPI is a modern, fast (high performance), web framework for building APIs with Python 3.6+.
# It's designed to be fast, scalable, and easy to use.
# FastAPI is built on top of standard Python type hints and supports OpenAPI, automatically generating API documentation.
# It also supports automatic API routes, request and response validation, and more.
# FastAPI is a great choice for building APIs, especially for data-intensive applications.

# pip install fastapi uvicorn
# uvicorn main:app --reload
'''
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to FastAPI!"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}

'''

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float
    description: str = None


# Request Parameters and Validation
@app.post("/items/")
def create_item(item: Item):
    return {"item": item}


# Query Parameters
@app.get("/search/")
def search_items(q: str = None, limit: int = 10):
    return {"query": q, "limit": limit}


# Path Parameters
@app.get("/users/{user_id}")
def get_user(user_id: int):
    return {"user_id": user_id}


# HTTP Methods
@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_id": item_id, "item": item}

