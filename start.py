from fastapi import FastAPI, Path

app = FastAPI()
inverntory = {
    1: {
    "name": "milk",
    "price": "10.00",
    "brand": "Ideal",

    }
}
# creating end point with path parameter
@app.get("/get-items/{itemId}")
def get_items(itemId: int = Path(None, description = "the id of the item")):
    return inverntory.get(itemId)
