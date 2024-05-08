class Class:

    __students_count = 22

    def __init__(self, name):
        self.name = name
        self.students = []
        self.grades = []

    def add_student(self, student_name, student_grade):
        self.student_name = student_name
        self.student_grade = student_grade
        if self.__students_count > 0:
            self.students.append(student_name)
            self.grades.append(student_grade)

    def get_average_grade(self):
        result =  float(f"{sum(self.grades) / len(self.grades):.2f}")
        return result

    def __repr__(self):
        return f"The students in {self.name}: {', '.join(self.students)}. Average grade: {self.get_average_grade()}"