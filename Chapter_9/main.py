from fastapi import FastAPI, Path, Query
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

students = {
    1: {
        "name": "John",
        "age": 20,
        "city": "New York"
    },
    2: {
        "name": "Jane",
        "age": 21,
        "city": "Los Angeles"
    },
    3: {
        "name": "Jim",
        "age": 22,
        "city": "Chicago"
    }
}

#Pydantic Model
class Item(BaseModel):
    Id: int
    Name: str
    Price: float

#Declare Data Type
def dataType(number: int, string: str, boolean: bool, list: list[str], dict: dict[str, int]):
    return {
        "number": number,
        "string": string,
        "boolean": boolean,
        "list": list,
        "dict": dict
    }

def union(union: int | str):
    return {"Type": str(type(union))}

@app.get("/")
def index():
    return "<h1>Hello, World!</h1>"

@app.get("/union/{test}")
def get_union(test: int | str):
    return union(test)

@app.get("/data")
def get_data():
    return dataType(number=1, 
                    string="Hello", 
                    boolean=True, 
                    list=["item1", "item2", "item3"],
                    dict={"item1": 1, "item2": 2, "item3": 3})

@app.post("/api/post/item")
def post_data(item: Item):
    return item

#Path Parameters, Query Parameters
@app.get("/students/{student_id}")
def read_item(student_id: int = Path(description="The ID of the student you want to view", le = 3, gt = 0),
            student_name: Optional[str] = Query(None, description="The name of the student you want to view")):
    return students[student_id]