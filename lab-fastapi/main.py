from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

'''@app.get("/")
async def root():
    return {"message": "Hello World"}
'''
class StudentCreateSchema(BaseModel):
    first_name: str
    last_name: str

    '''def add_student( self , status):
            input("Entern fname:")
            input("Enter lname")
            self.status = status'''

class Student(StudentCreateSchema):
    id: int
STUDENTS = {}

@app.get("/students")
async def get_students():
    return STUDENTS

@app.post("/students")
async def create_student(student: StudentCreateSchema):
    id = len(STUDENTS) + 1
    new_student = Student(**student.dict(), id=id)
    STUDENTS[id] = new_student
    return new_student
