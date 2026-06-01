from pydantic import BaseModel

class Student(BaseModel):
    id: int
    name: str
    age: int

students = [
    {"id": 1, "name": "Parth", "age": 20},
    {"id": 2, "name": "Rahul", "age": 21}
]