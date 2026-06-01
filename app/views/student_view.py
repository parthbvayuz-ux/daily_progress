from fastapi import APIRouter
from app.models.student import Student
from app.controller.student_controller import StudentController

router = APIRouter()

@router.get("/")
def home():
    return {"message": "Student API"}

@router.get("/students")
def get_students():
    return StudentController.get_all_students()