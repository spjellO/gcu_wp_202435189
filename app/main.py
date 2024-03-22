from fastapi import FastAPI
from typing import Union

app = FastAPI()

@app.get("/")
def root():
    return { "message": "Hello Root!" }

@app.get("/test")
def test():
    return "Here is testing page"

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}