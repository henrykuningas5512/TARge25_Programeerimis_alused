"""School class which stores information about courses and students."""


class School:
    """School class, do not change."""

    def __init__(self, name):
        """Initialize school with name."""
        self.name = name
        self.students = []
        self.courses = []
        self._next_id = 1

    def add_course(self, course):
        """Add course if not already present."""
        if course not in self.courses:
            self.courses.append(course)

    def add_student(self, student):
        """Add student if not already present and assign id."""
        if student not in self.students:
            self.students.append(student)
            student.set_id(self._next_id)
            self._next_id += 1

    def add_student_grade(self, student, course, grade):
        """Add grade to student and course if both exist."""
        if student in self.students and course in self.courses:
            student.add_grade(course, grade)
            course.add_grade(student, grade)

    def get_students(self):
        """Return list of students."""
        return self.students

    def get_courses(self):
        """Return list of courses."""
        return self.courses

    def get_students_ordered_by_average_grade(self):
        """Return students sorted by average grade descending."""
        return sorted(
            self.students,
            key=lambda student: student.get_average_grade(),
            reverse=True
        )
