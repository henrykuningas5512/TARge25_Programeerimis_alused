"""Course class with name and grades."""


class Course:
    """Course class, do not change."""

    def __init__(self, name: str):
        """Initialize course with name."""
        self.name = name
        self.grades = []

    def add_grade(self, student, grade):
        """Add grade for a student."""
        self.grades.append((student, grade))

    def get_grades(self):
        """Return list of grades."""
        return self.grades

    def get_average_grade(self):
        """Return average grade or -1 if none."""
        if not self.grades:
            return -1
        return sum(grade for _, grade in self.grades) / len(self.grades)

    def __repr__(self):
        """Return course name."""
        return self.name
