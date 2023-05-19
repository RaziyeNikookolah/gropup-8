from fastapi import FastAPI

app=FastAPI()

@app.get('/{id}')
def test(id: int):
    ret
