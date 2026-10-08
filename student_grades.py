# Reviewed under SE2 coding standards guidelines
MIN_GRADE = 0
MAX_GRADE = 100
PASSING_GRADE = 60
HONOR_ROLL_GRADE = 90
LETTER_GRADES = [(90, "A"), (80, "B"), (70, "C"), (60, "D")]
FAILING_LETTER = "F"
SEPARATOR = "-" * 40


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

    def is_on_honor_roll(self):
        return self.calculate_average() >= HONOR_ROLL_GRADE

    def remove_grade_by_index(self, index):
        if not 0 <= index < len(self.grades):
            raise IndexError(
                f"Grade index {index} is out of range "
                f"(valid: 0 to {len(self.grades) - 1})."
            )
        return self.grades.pop(index)

    def remove_grade_by_value(self, value):
        try:
            self.grades.remove(float(value))
        except ValueError as error:
            raise ValueError(
                f"Grade {value} was not found for {self.name}."
            ) from error
        return float(value)

    def get_summary_report(self):
        status = "Passed" if self.has_passed() else "Failed"
        return "\n".join([
            SEPARATOR,
            f"Student ID:     {self.student_id}",
            f"Student Name:   {self.name}",
            f"Grades Count:   {len(self.grades)}",
            f"Average Grade:  {self.calculate_average():.2f}",
            f"Letter Grade:   {self.get_letter_grade()}",
            f"Status:         {status}",
            f"Honor Roll:     {self.is_on_honor_roll()}",
            SEPARATOR,
        ])


def create_student(student_id, name):
    try:
        return Student(student_id, name)
    except ValueError as error:
        print(f"Error creating student: {error}")
        return None


def add_grades(student, grades):
    for grade in grades:
        try:
            student.add_grade(grade)
        except (TypeError, ValueError) as error:
            print(f"Error adding grade to {student.name}: {error}")


def remove_grade(student, index=None, value=None):
    try:
        if index is not None:
            removed = student.remove_grade_by_index(index)
        else:
            removed = student.remove_grade_by_value(value)
        print(f"Removed grade {removed} from {student.name}.")
    except (IndexError, ValueError) as error:
        print(f"Error removing grade: {error}")


def main():
    print("== Invalid students ==")
    create_student("", "Ana Torres")
    create_student("S000", "   ")

    print("\n== Adding grades ==")
    ana = create_student("S001", "Ana Torres")
    luis = create_student("S002", "Luis Vera")
    maria = create_student("S003", "Maria Leon")
    add_grades(ana, [95.0, 92.5, 88, "Ninety", 150])
    add_grades(luis, [55, 61.5, 40, -5])
    add_grades(maria, [78, 85, 81])

    print("\n== Removing grades ==")
    remove_grade(ana, value=88)
    remove_grade(luis, index=1)
    remove_grade(maria, value=99)
    remove_grade(maria, index=10)

    print("\n== Summary reports ==")
    for student in (ana, luis, maria):
        print(student.get_summary_report())


if __name__ == "__main__":
    main()
