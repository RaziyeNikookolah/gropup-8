from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    id: int
    name: str


items = [
    {"id": 1, "name": "sara"},
    {"id": 2, "name": "maryam"},
    {"id": 3, "name": "bahar"},
]


@app.get("/items/{item_id}")
def read_item(item_id: int):
    found_item = list(filter(lambda item: item["id"] == item_id, items))
    if found_item:
        return found_item[0]
    raise HTTPException(status_code=HTTPException.HTTP_, detail="Item not found")


@app.post("/items")
def create_item(item: Item):
    items.append(item.dict())
    return {"message": "Added.."}
