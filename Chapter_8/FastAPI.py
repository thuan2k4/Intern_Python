from fastapi import FastAPI, Path
import asyncio
app = FastAPI()

data = {
    1: {"name": "John", "age": 25},
    2: {"name": "Jane", "age": 30},
    3: {"name": "Jim", "age": 35},
}

async def get_item_for_async(item_id: int):
    await asyncio.sleep(2)
    return data.get(item_id)

@app.get("/")
def read_root():
    return {"message": "Hello World"}

@app.get("/items/{item_id}")
async def get_item_for_sync(item_id: int):
    item = await get_item_for_async(item_id)
    return item

#127.0.0.1:8000/docs to use swagger API