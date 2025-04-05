from fastapi import FastAPI, Path, Body
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

class Student(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None
    city: Optional[str] = None

next_id = 4

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

#Create
@app.post("/students/", response_model=Student)
def create(student: Student):
    global next_id
    new_student = {
        "name": student.name,
        "age": student.age,
        "city": student.city
    }
    students[next_id] = new_student
    next_id += 1
    return new_student

#Read
@app.get("/students/")
def read():
    return students #JSON Datatype

#Patch instead of Put (update one or more fields)
@app.patch("/students/{student_id}", response_model=Student)
def update(student_id: int = Path(description="Get Student by Id", ge = 1, le = next_id - 1),
            student: Optional[Student] = Body(default=None, description="Update Student")):

    current_student = students[student_id]

    update_student = student.dict(exclude_unset=True) 
    #exclude_unset=True: Only update the fields that are not None
    
    current_student.update(update_student)
    students[student_id] = current_student

    return students[student_id]

#Put
@app.put("/students/{student_id}", response_model=Student)
def update(student_id: int = Path(description="Get Student by Id", ge = 1, le = next_id - 1),
            student: Student = Body(description="Update Student")):
    
    students[student_id] = student.dict()
    return students[student_id]

#Delete
@app.delete("/students/{student_id}", response_model=Student)
def delete(student_id: int = Path(description="Get Student by Id", ge = 1, le = next_id - 1)):
    Delete_student = students[student_id]
    del students[student_id]
    return Delete_student
