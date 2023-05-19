from fastapi import FastAPI
from pydantic import BaseModel
from products import product_list

app = FastAPI()


app.get('/product/{id}')
def get_item(id: int):
    product_list.get(id)


app.post('/product/')
def add_item():
    ...