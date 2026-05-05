"""Student main file"""
from student import Student


if __name__ == '__main__':
    student1 = Student("Ann", ["Programming", "Maths", "Lithology"], 3.2)
    student2 = Student("Josh", ["Maths", "English", "Politics"], 2.0)
    student3 = Student("Bush", ["Politics"], 0.5)
    student4 = Student("Marcus", ["Web application", "Computers", "Artificial Intelligence"], 4.2)
    students = [student1, student2, student3, student4]
    print(filter_by_course(students, "Maths"))  # -> [Ann, Josh]
    print(is_failing(student3))  # -> True
    print(is_failing(student1))  # -> False
    print(succeeding_students(students))  # -> [Ann, Josh, Marcus]
    print(failing_students(students))  # -> [Bush]
    print(sort_by_best_grade(students))  # -> [Marcus, Ann, Josh]
    print(sort_by_worst_grade(students))  # -> [Josh, Ann, Marcus]
