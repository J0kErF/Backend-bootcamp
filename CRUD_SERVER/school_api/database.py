import json

class Database:
    def __init__(self, filename):
        self.filename = filename

    def read_data(self):
        try:
            with open(self.filename, 'r') as file:
                data = json.load(file)
        except FileNotFoundError:
            data = {}
        return data

    def write_data(self, data):
        with open(self.filename, 'w') as file:
            json.dump(data, file)

    def add_student(self, student):
        data = self.read_data()
        student_dict = student.to_dict()
        data[student.id] = student_dict
        self.write_data(data)

    def delete_student(self, student_id):
        data = self.read_data()
        if student_id in data:
            del data[student_id]
            self.write_data(data)
            return True
        else:
            return False

    def get_student(self, student_id):
        data = self.read_data()
        return data.get(student_id, None)

    def get_all_students(self):
        data = self.read_data()
        return data
