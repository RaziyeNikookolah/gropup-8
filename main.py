from fastapi import FastAPI, HTTPException, Request, status
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from fastapi.responses import HTMLResponse


app = FastAPI()

template = Jinja2Templates(directory="template")


class Item(BaseModel):
    id: int
    username: str


items = [
    {"id": 1, "name": "ali"},
    {"id": 2, "name": "zahra"},
    {"id": 3, "name": "akbar"},
    {"id": 4, "name": "maryam"},
    {"id": 5, "name": "ahmad"},
    {"id": 6, "name": "sara"},
]


item_list = list(map(lambda x: Item(id=x["id"], username=x["name"]), items))


@app.get("/items/{id}")
def get_by_id(id: int):
    for item in item_list:
        if item.id == id:
            return item
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)


@app.post("/items/")
def post_item(item: Item):
    items.append(item.dict())
    return {"message": "item created"}


# @app.get('/items/')
# def get_items(item_per_page: int, page_num: int):
#     result=items[(page_num-1)*item_per_page:page_num*item_per_page]
#     totalpage=len(items)//item_per_page+(1 if len(items) % item_per_page else 0)
#     return {'items': result,
#     'page':page_num,
#     'items_count':len(result),
#     'total_pages':totalpage,
#     'prev_page': f'http://127.0.0.1:8000/items/?page_num={page_num-1}&item_per_page={item_per_page}' if page_num-1>0 else None,
#     'next_page': f'http://127.0.0.1:8000/items/?page_num={page_num+1}&item_per_page={item_per_page}' if page_num+1<=totalpage else None
#     }


@app.get("/items/")
def get_items(item_per_page: int, page_num: int):
    result = item_list[(page_num - 1) * item_per_page : page_num * item_per_page]
    totalpage = len(item_list) // item_per_page + (
        1 if len(item_list) % item_per_page else 0
    )
    if page_num > totalpage:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return {
        "items": result,
        "page": page_num,
        "items_count": len(result),
        "total_pages": totalpage,
        "prev_page": f"http://127.0.0.1:8000/items/?page_num={page_num-1}&item_per_page={item_per_page}"
        if page_num - 1 > 0
        else None,
        "next_page": f"http://127.0.0.1:8000/items/?page_num={page_num+1}&item_per_page={item_per_page}"
        if page_num + 1 <= totalpage
        else None,
    }


@app.get("/item/home/", response_class=HTMLResponse)
def read_item(request: Request):
    return template.TemplateResponse(
        "index.html", {"request": request, "items": item_list}
    )
