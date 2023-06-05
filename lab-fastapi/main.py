from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

import students

app = FastAPI()

app.include_router(students.router, prefix="/students")

# Define Pydantic models

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

# Endpoint to get all students
@app.get("/students")
async def get_students():
    return STUDENTS

# Endpoint to create a new student
@app.post("/students")
async def create_student(student: StudentCreateSchema):
    id = len(STUDENTS) + 1
    new_student = Student(**student.dict(), id=id)
    STUDENTS.append(new_student)  # Append the new student to the list
    return new_student

# Endpoint to get a student by ID
@app.get("/students/{student_id}")
async def read_item(student_id: int):
    if student_id not in [student["id"] for student in STUDENTS]:
        raise HTTPException(status_code=404, detail="Student not found")
    student = next(student for student in STUDENTS if student["id"] == student_id)
    return {"Student ID": student}

# Endpoint to remove a student by ID
@app.delete("/students/{student_id}")
async def remove_student(student_id: int):
    for student in STUDENTS:
        if student["id"] == student_id:
            STUDENTS.remove(student)
            return {"message": f"Student with ID {student_id} has been removed."}
    raise HTTPException(status_code=404, detail="Student not found")

# Endpoint to update a student's first name and last name by ID
@app.put("/students/{student_id}")
async def update_student(student_id: int, updated_student: StudentUpdateSchema):
    if student_id not in [student["id"] for student in STUDENTS]:
        raise HTTPException(status_code=404, detail="Student not found")
    for student in STUDENTS:
        if student["id"] == student_id:
            student["first_name"] = updated_student.first_name
            student["last_name"] = updated_student.last_name
            return {"message": f"Student with ID {student_id} has been updated."}
    raise HTTPException(status_code=404, detail="Student not found")