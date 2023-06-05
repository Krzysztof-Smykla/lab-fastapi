from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from random import *

app = FastAPI()


class StudentCreateSchema(BaseModel):
    first_name: str
    last_name: str

    class Config:
        schema_extra = {"message": "Hello World"}


class Student(BaseModel):
    id: int
    first_name: str
    last_name: str


class StudentUpdateSchema(BaseModel):
    student_id: int
    first_name: str
    last_name: str


# Assume you have a list of students
STUDENTS = [
    {"id": 1, "name": "John Doe"},
    {"id": 2, "name": "Jane Smith"},
    {"id": 3, "name": "Alex Johnson"},
]

@app.get("/students")
async def get_students():
    return STUDENTS

@app.post("/students")
async def create_student( student: StudentCreateSchema):
    id = len(STUDENTS) + 1
    # id = random.randint(0,9) + 10
    new_student = Student(**student.dict(), id=id)
    STUDENTS[id] = new_student
    return new_student

@app.get("/STUDENTS/student_id")
async def read_item( student_id: int ):
    if student_id not in STUDENTS:
        raise HTTPException(status_code=404, detail="Student not found")
    return {"Student ID": STUDENTS[student_id]}

@app.delete("/students/{student_id}")
async def remove_student(student_id: int):
    for student in STUDENTS:
        if student["id"] == student_id:
            STUDENTS.remove(student)
            return {"message": f"Student with ID {student_id} has been removed."}

    raise HTTPException(status_code=404, detail="Student not found")

    @app.get("/students/{student_id}")
    async def read_item2(student_id: int, first_name: str, last_name: str ):
        if student_id not in STUDENTS:
            raise HTTPException(status_code=404, detail="Student not found")
        new_student = StudentUpdateSchema(first_name=first_name, last_name=last_name, id=student_id)
        STUDENTS[student_id] = new_student
        return {"Student ID": STUDENTS[student_id]}




# uvicorn KOD:app --reload
