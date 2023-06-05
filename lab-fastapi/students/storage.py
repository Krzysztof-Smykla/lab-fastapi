from functools import lru_cache
from .schema import Student

STUDENTS: dict[int, Student] = {}

@lru_cache(maxsize=1)
def get_students_storage() -> dict[int, Student]:
    return STUDENTS


STUDENTS = [
    {"id": 1, "name": "John Doe"},
    {"id": 2, "name": "Jane Smith"},
    {"id": 3, "name": "Alex Johnson"},
]

# Endpoint to get all students
@app.get("/students")
async def get_students():
    return STUDENTS