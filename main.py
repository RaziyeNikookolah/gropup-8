from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    id: int
    name: str


items = [
    {"id": 1, "name": "abbas"},
    {"id": 2, "name": "mohammad"},
    {"id": 3, "name": "vahid"},
]


@app.get("/items/{item_id}")
def read_item(item_id: int):
    for item in items:
        if item["id"] == item_id:
            return item
    raise HTTPException(status_code=404, detail="Item not found")


@app.post("/items")
def create_item(item: Item):
    items.append(item.dict())
    return {"message": "Item created"}
