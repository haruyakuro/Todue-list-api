from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}

@app.patch("/items/{item_id}")
def patch_item(item_id:int,name:str,kind:str,date:str,score:int):
    return '編集完了しました'
@app.post("/items/")
def add_item(name: str, kind: str, date: str, score: int):
    return "取得完了"
