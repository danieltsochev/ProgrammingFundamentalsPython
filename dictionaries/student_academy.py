students_grade_count = int(input())

student_book = {}

for iteration in range(students_grade_count):
    current_name = input()
    current_grade = float(input())

    if current_name not in student_book.keys():
        student_book[current_name] = []
    student_book[current_name] += [current_grade]


for current_name, current_grade in student_book.items():
    if sum(current_grade) / len(current_grade) >= 4.50:
        print(f"{current_name} -> {sum(current_grade) / len(current_grade):.2f}")