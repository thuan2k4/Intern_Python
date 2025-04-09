from fastapi import FastAPI, Request
from pydantic import BaseModel
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from pathlib import Path

class Math(BaseModel):
    number1: float
    number2: float
    operation: str

app = FastAPI()

templates = Jinja2Templates(directory="templates")

# Lấy đường dẫn tuyệt đối của thư mục static
static_dir = Path(__file__).parent / "static"

# Mount thư mục static
app.mount("/static", StaticFiles(directory=static_dir), name="static")

@app.get("/")
def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/api/v1/math")
def math(math: Math):
    result = 0
    
    if math.operation == "add":
        result = math.number1 + math.number2
    elif math.operation == "subtract":
        result = math.number1 - math.number2
    
    return result
