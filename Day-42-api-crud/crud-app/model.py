from sqlalchemy import Table, Column, Integer, String
from database import metadata



items = Table(
    "items",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String(255)),
    Column("description", String(255)),
    Column("price", Integer),
)
