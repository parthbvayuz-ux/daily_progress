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

@router.post("/students")
def add_student(student: Student):
    return StudentController.add_student(student)

@router.put("/students/{student_id}")
def update_student(
    student_id: int,
    updated_student: Student
):
    return StudentController.update_student(
        student_id,
        updated_student
    )

@router.delete("/students/{student_id}")
def delete_student(student_id: int):
    return StudentController.delete_student(
        student_id
    )