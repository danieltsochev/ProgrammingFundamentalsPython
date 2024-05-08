def adding_student_info(student_dict, course_dict, command):
    max_points = 0
    adding_command = command.split("-")
    name, course, score = adding_command[0], adding_command[1], int(adding_command[2])
    if name not in student_dict.keys():
        student_dict[name] = 0

    if student_dict[name] < score:
        student_dict[name] = score

    if course not in course_dict.keys():
        course_dict[course] = 1
    else:
        course_dict[course] += 1
    return student_dict, course_dict


def removing_student_info(student_dict, command):
    removing_command = command.split("-")
    name, action = removing_command[0], removing_command[1]
    if name in student_dict.keys():
        del student_dict[name]
    return student_dict


courses = {}

student_info = {}

while True:
    current_info = input()

    if "exam finished" in current_info:
        break

    elif "banned" in current_info:
        removing_student_info(student_info, current_info)

    else:
        adding_student_info(student_info, courses, current_info)

print("Results:")
for key, value in student_info.items():
    print(f"{key} | {value}")
print("Submissions:")
for key, value in courses.items():
    print(f"{key} - {value}")