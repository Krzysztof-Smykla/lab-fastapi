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

