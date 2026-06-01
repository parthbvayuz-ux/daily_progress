from fastapi import HTTPException
from app.models.student import students

class StudentController:

    @staticmethod
    def get_all_students():
        return students