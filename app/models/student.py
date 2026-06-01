from pydantic import BaseModel,Field

class Student(BaseModel):
    id: int
    name: str=Field(min_length=3,max_length=50)
    age: int=Field(ge=18,le=88)

students = [
    {"id": 1, "name": "Parth", "age": 20},
    {"id": 2, "name": "Rahul", "age": 21}
]