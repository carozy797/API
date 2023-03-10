from fastapi import FastAPI, Path, Query, HTTPException
from typing import Optional
from pydantic import BaseModel

class Item(BaseModel):
    name: str
    price: float
    brand: Optional[str] = None
# to allow update for one at a time
class UpdateItem(BaseModel):
    name: Optional[str] = None
    price: Optional[float] = None
    brand: Optional[str] = None


app = FastAPI()
inventory = {}
# creating end point with path parameter
@app.get("/get-items/{itemId}")
def get_items(itemId: int = Path(None, description = "the id of the item")):
    return inventory.get(itemId, "wrong Id specified")

# getting item by name using query
@app.get("/get-items-by-name")
def get_items_by_name(name : str = Query(None, description = "the name of the item", title = "Name")):
    for item_id in inventory:
        if inventory[item_id].name == name:
            return inventory[item_id]
    return {"Data": "Not found"}

# posting data 
@app.post("/create-item")
def create_item(item : Item, item_id: int):
    if item_id in inventory:
        return {"error": "Item already exists"}
    inventory[item_id] = item
    return inventory[item_id]

@app.put("/update-item")
def update_item(item: UpdateItem, item_id: int):
    if item_id not in inventory:
        return {"error": "Item does not exist"}
    if item.name != None:
      inventory[item_id].name = item.name
    if item.brand != None:
      inventory[item_id].brand = item.brand
    if item.price != None:
      inventory[item_id].price = item.price
    return inventory[item_id]

# creating delete endpt
@app.delete("delete-item")
def delete_item(item_id: int = Query(...,description = "Id of the item to delete", gt = 0)):
    if item_id not in inventory:
        return {"error": "Id of the item does not exist"}
    del inventory[item_id]