from fastapi import FastAPI, Request, Form, HTTPException
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from sqlalchemy import insert, select, update, delete
from database import engine
from model import items

app = FastAPI()

# Mount templates
templates = Jinja2Templates(directory="app/templates")

@app.get("/")
async def read_items(request: Request):
    query = select(items)
    with engine.connect() as conn:
        result = conn.execute(query).fetchall()
    return templates.TemplateResponse("index.html", {"request": request, "items": result})

@app.get("/create/")
async def create_item_form(request: Request):
    return templates.TemplateResponse("create.html", {"request": request})

@app.post("/create/")
async def create_item(name: str = Form(...), description: str = Form(...), price: int = Form(...)):
    query = insert(items).values(name=name, description=description, price=price)
    with engine.connect() as conn:
        conn.execute(query)
    return RedirectResponse("/", status_code=302)

@app.get("/update/{item_id}/")
async def update_item_form(item_id: int, request: Request):
    query = select(items).where(items.c.id == item_id)
    with engine.connect() as conn:
        item = conn.execute(query).fetchone()
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return templates.TemplateResponse("update.html", {"request": request, "item": item})

@app.post("/update/{item_id}/")
async def update_item(item_id: int, name: str = Form(...), description: str = Form(...), price: int = Form(...)):
    query = update(items).where(items.c.id == item_id).values(name=name, description=description, price=price)
    with engine.connect() as conn:
        conn.execute(query)
    return RedirectResponse("/", status_code=302)

@app.post("/delete/{item_id}/")
async def delete_item(item_id: int):
    query = delete(items).where(items.c.id == item_id)
    with engine.connect() as conn:
        conn.execute(query)
    return RedirectResponse("/", status_code=302)
