from fastapi import HTTPException
from app.models.student import students

class StudentController:

    @staticmethod
    def get_all_students():
        return students
    
    @staticmethod
    def add_student(student):
        for s in students:
            if s["id"] == student.id:
                raise HTTPException(
                    status_code=400,
                    detail="Student ID already exists"
                )

        students.append(student.dict())

        return {
            "message": "Student added successfully",
            "student": student
            }
    @staticmethod
    def update_student(student_id: int, updated_student):
        for index, student in enumerate(students):

            if student["id"] == student_id:

                students[index] = updated_student.dict()

                return {
                    "message": "Student updated successfully",
                    "student": updated_student
                }

        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )
    
    @staticmethod
    def delete_student(student_id: int):

        for index, student in enumerate(students):

            if student["id"] == student_id:

                deleted_student = students.pop(index)

                return {
                    "message": "Student deleted successfully",
                    "student": deleted_student
                }

        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )