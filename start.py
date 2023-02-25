from fastapi import FastAPI, Path, Query
from typing import Optional
from pydantic import BaseModel

class Item(BaseModel):
    name: str
    price: float
    brand: Optional[str] = None


app = FastAPI()
inventory = {}
# creating end point with path parameter
@app.get("/get-items/{itemId}")
def get_items(itemId: int = Path(None, description = "the id of the item")):
    return inventory.get(itemId)
# getting item by name using query
@app.get("/get-items-by-name")
def get_items_by_name(name : str = Query(None, description = "the name of the item", title = "Name")):
    for item_id in inventory:
        if inventory[item_id].name == name:
            return inventory[item_id]
    return {"Data": "Not found"}

