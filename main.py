from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

#define a model for the item
class Item(BaseModel):
    id : int
    name : str
    description : str

# Create a list of dictionary objects to act as items data
items = [
    {"id": 1, "name": "Item 1", "description": "Description 1"},
    {"id": 2, "name": "Item 2", "description": "Description 2"},
    {"id": 3, "name": "Item 3", "description": "Description 3"},
]

#route to get an item by ID
@app.get("/items/{item_id}")
def get_item(item_id: int):
    for item in items :
        if item['id'] == item_id :
            return item
    
    raise HTTPException(status_code = 404, detail= "file not found")

#route to create new item 
@app.post("/items")
def create_item(item: Item):
    items.append(item.dict())
    return {"message": "Item created successfully."}

#run the application with uvicorn
if __name__ == "__main__" :
    import uvicorn
    uvicorn.run("main:app", host="localhost", port=8000, log_level="info")