class Student:
    def __init__(self, student_id: int, name: str, age: int, classes: list):
        self.id = student_id
        self.name = name
        self.age = age
        self.classes = classes

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'age': self.age,
            'classes': self.classes
        }