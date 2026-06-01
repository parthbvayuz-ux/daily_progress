class Student:
    def __init__(self, roll_no, name):
        self.roll_no = roll_no
        self.name = name
        self.marks = []
    def add_mark(self, mark):
        if mark < 0 or mark > 100:
            raise ValueError("Marks must be between 0 and 100")
        self.marks.append(mark)
    def average(self):
        if not self.marks:
            return 0
        return sum(self.marks) / len(self.marks)
    def display(self):
        print(f"Roll No: {self.roll_no}")
        print(f"Name: {self.name}")
        print(f"Marks: {self.marks}")
        print(f"Average: {self.average():.2f}")
class StudentManager:
    def __init__(self):
        self.students = {}
    def add_student(self, roll_no, name):
        if roll_no in self.students:
            raise Exception("Student already exists")
        self.students[roll_no] = Student(roll_no, name)
    def add_marks(self, roll_no, mark):
        if roll_no not in self.students:
            raise KeyError("Student not found")
        self.students[roll_no].add_mark(mark)
    def get_topper(self):
        if not self.students:
            return None
        topper = max(
            self.students.values(),
            key=lambda student: student.average()
        )
        return topper
    def display_all(self):
        for student in self.students.values():
            student.display()
            print("-" * 30)
try:
    manager = StudentManager()
    manager.add_student(1, "Parth")
    manager.add_student(2, "Rahul")
    manager.add_marks(1, 95)
    manager.add_marks(1, 88)
    manager.add_marks(2, 78)
    manager.add_marks(2, 82)
    manager.display_all()
    topper = manager.get_topper()
    print("\nTopper:")
    topper.display()
except ValueError as e:
    print("Value Error:", e)
except KeyError as e:
    print("Key Error:", e)
except Exception as e:
    print("Error:", e)