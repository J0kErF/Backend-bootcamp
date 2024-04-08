from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from database import Database
from models import Student

app = FastAPI()
db = Database("students_data.txt")

class StudentModel(BaseModel):
    id: int
    name: str
    age: int
    classes: list

@app.post("/students/")
def create_student(student: StudentModel):
    new_student = Student(student.id, student.name, student.age, student.classes)
    db.add_student(new_student)
    return {"message": "Student added successfully"}

@app.get("/students/{student_id}")
def read_student(student_id: int):
    student_data = db.get_student(student_id)
    if student_data:
        return student_data
    else:
        raise HTTPException(status_code=404, detail="Student not found")

@app.get("/students/")
def read_all_students():
    return db.get_all_students()

@app.delete("/students/{student_id}")
def delete_student(student_id: int):
    if db.delete_student(student_id):
        return {"message": "Student deleted successfully"}
    else:
        raise HTTPException(status_code=404, detail="Student not found")
