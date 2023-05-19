from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from products import product_list


class Products(BaseModel):
    name: str
    price: int
    category: str


app = FastAPI()


@app.get("/product", response_model=dict[int, Products])
def all_item():
    return product_list.items()


@app.get("/product/{id}")
def get_item(id: int) -> dict:
    item = product_list.get(id)
    if not item:
        raise HTTPException(status_code=404, detail="product doesn't exists ")
    return item


@app.post("/product/")
def add_item(product: Products):
    last_id = max(product_list.keys())
    product_list[last_id+1] = product
    
