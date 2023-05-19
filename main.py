from fastapi import FastAPI
from typing import List

app = FastAPI()

# create a list of dictionary objects to simulate a real system
items = [
    {"id": 1, "name": "kiana", "description": "description1"},
    {"id": 2, "name": "katayoon", "description": "description2"},
    {"id": 3, "name": "gity", "description": "description3"}
]

# GET /items/{item_id}: Return an item given an id
@app.get("/items/{item_id}")
def read_item(item_id: int):
    for item in items:
        if item["id"] == item_id:
            return item
    # If the item is not found, return an HTTP 404 Not Found response
    return {"error": "Item not found."}

# POST /items: Create a new item in the system
@app.post("/items")
def create_item(item: dict):
    items.append(item)
    return {"message": "Item created successfully."}