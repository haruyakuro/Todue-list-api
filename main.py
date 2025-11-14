from fastapi import FastAPI
from model import ItemCreate, ItemUpdate
from api import add_item as add_item_api, get_item as get_item_api, get_all_items as get_all_items_api, update_item as update_item_api

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/")
def get_all_items():
    return get_all_items_api()


@app.get("/items/{item_id}")
def read_item(item_id: int):
    return get_item_api(item_id)


@app.post("/items/")
def add_item(item: ItemCreate):
    return add_item_api(item)


@app.patch("/items/{item_id}")
def patch_item(item_id: int, item: ItemUpdate):
    return update_item_api(item_id, item)
