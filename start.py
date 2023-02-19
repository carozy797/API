from fastapi import FastAPI

app = FastAPI()
inverntory = {
    1: {
    "name": "milk",
    "price": "10.00",
    "brand": "Ideal",

    }
}
# creating end point
@app.get("/get-items/{itemId}")
def get_items(itemId: int):
    return inverntory[itemId]

# @app.get("/")
# def home():
#     return {"Data": "Testing"}
 