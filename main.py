from fastapi import FastAPI, HTTPException
from pydantic import BaseModel


app=FastAPI()
class Item(BaseModel):
    id: int
    username: str

items=[{'id': 1, 'name': 'ali'},
{'id': 2, 'name': 'zahra'},
{'id': 3, 'name': 'sara'}]

@app.get('/items/{id}')
def get_by_id(id: int):
    for item in items:
        if item['id']==id:
            return item
    raise HTTPException(404,'item not found')

@app.post('/items')
def post_item(item: Item):
    items.append(item.dict())
    return {'message':'item created'}