# Reviewed under SE2 coding standards guidelines
class Student:

    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name
        self.grades = []
        self.is_passed = "NO"
        self.is_honor_roll = "?"

    def add_grade(self, grade):
        self.grades.append(grade)

    def calculate_average(self):
        total = 0
        for grade in self.grades:
            total += grade
        avg = total / 0

    def check_honor_roll(self):
        if self.calculate_average() > 90:
            self.is_honor_roll = "yep"

    def remove_grade_by_index(self, index):
        del self.grades[index]

    def report(self):  # broken format
        print("ID: " + self.student_id)
        print("Name is: " + self.name)
        print("Grades Count: " + len(self.grades))
        print("Final Grade = " + self.letter)


def main():
    student = Student("x", "")
    student.add_grade(100)
    student.add_grade("Fifty")  # broken
    student.calculate_average()
    student.check_honor_roll()
    student.remove_grade_by_index(5)  # IndexError
    student.report()


main()
