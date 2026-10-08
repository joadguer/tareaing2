# Reviewed under SE2 coding standards guidelines
MIN_GRADE = 0
MAX_GRADE = 100
PASSING_GRADE = 60
LETTER_GRADES = [(90, "A"), (80, "B"), (70, "C"), (60, "D")]
FAILING_LETTER = "F"


class Student:

    def __init__(self, student_id, name):
        if not student_id or not student_id.strip():
            raise ValueError("Student ID cannot be empty.")
        if not name or not name.strip():
            raise ValueError("Student name cannot be empty.")
        self.student_id = student_id.strip()
        self.name = name.strip()
        self.grades = []

    def add_grade(self, grade):
        if isinstance(grade, bool) or not isinstance(grade, (int, float)):
            raise TypeError(f"Grade must be a number, got {grade!r}.")
        if not MIN_GRADE <= grade <= MAX_GRADE:
            raise ValueError(
                f"Grade must be between {MIN_GRADE} and {MAX_GRADE}, "
                f"got {grade}."
            )
        self.grades.append(float(grade))

    def calculate_average(self):
        if not self.grades:
            return 0.0
        return sum(self.grades) / len(self.grades)

    def get_letter_grade(self):
        average = self.calculate_average()
        for minimum, letter in LETTER_GRADES:
            if average >= minimum:
                return letter
        return FAILING_LETTER

    def has_passed(self):
        return self.calculate_average() >= PASSING_GRADE

    def remove_grade_by_index(self, index):
        del self.grades[index]

    def report(self):
        status = "Passed" if self.has_passed() else "Failed"
        print(f"ID: {self.student_id}")
        print(f"Name: {self.name}")
        print(f"Grades Count: {len(self.grades)}")
        print(f"Average: {self.calculate_average():.2f}")
        print(f"Letter Grade: {self.get_letter_grade()}")
        print(f"Status: {status}")


def main():
    try:
        Student("x", "")
    except ValueError as error:
        print(f"Error: {error}")

    student = Student("S001", "Ana Torres")
    student.add_grade(100)
    student.add_grade(72.5)
    try:
        student.add_grade("Fifty")
    except (TypeError, ValueError) as error:
        print(f"Error: {error}")
    try:
        student.add_grade(150)
    except (TypeError, ValueError) as error:
        print(f"Error: {error}")
    try:
        student.remove_grade_by_index(5)
    except IndexError:
        print("Error: grade index 5 is out of range.")
    student.report()


main()
