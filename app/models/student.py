from pydantic import BaseModel, Field, field_validator

class Student(BaseModel):
    id: int

    name: str = Field(
        min_length=3,
        max_length=50
    )

    age: int

    @field_validator("name")
    @classmethod
    def validate_name(cls, value):

        if not value.isalpha():
            raise ValueError(
                "Only letters allowed"
            )

        return value

    @field_validator("age")
    @classmethod
    def validate_age(cls, value):

        if value > 100 or value < 0:
            raise ValueError(
                "Invalid age"
            )

        return value


students = [
    {"id": 1, "name": "Parth", "age": 20},
    {"id": 2, "name": "Rahul", "age": 21}
]