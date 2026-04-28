"""Simple class."""
class Student:
    def __init__(self, name):
        self.finished = False
        self.name = name

student = Student("John")
print(student.name)       # John
print(student.finished)   # False
