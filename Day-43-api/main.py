from fastapi import FastAPI, Depends, Request, Form, HTTPException
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session

from database import SessionLocal, engine
from models import Base
import crud, schemas

# Initialize app and templates
app = FastAPI()
Base.metadata.create_all(bind=engine)
templates = Jinja2Templates(directory="templates")

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def read_items(request: Request, db: Session = Depends(get_db)):
    items = crud.get_items(db)
    return templates.TemplateResponse("index.html", {"request": request, "items": items})

@app.get("/create")
def create_form(request: Request):
    return templates.TemplateResponse("create.html", {"request": request})

@app.post("/create")
def create_item(
    name: str = Form(...),
    description: str = Form(...),
    price: int = Form(...),
    available: int = Form(...),
    db: Session = Depends(get_db)
):
    crud.create_item(db, schemas.ItemCreate(name=name, description=description, price=price, available=available))
    return RedirectResponse("/", status_code=302)




'''
Open the browser and navigate to:

Swagger UI: http://127.0.0.1:8000/docs
ReDoc: http://127.0.0.1:8000/redoc

'''