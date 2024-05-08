def add(function_list, function_command):
    add_command = function_command.split(":")
    action, lesson_title = add_command[0], add_command[1]
    if lesson_title not in function_list:
        function_list.append(lesson_title)
    return function_list


def insert(function_list, function_command):
    insert_command = function_command.split(":")
    action, lesson_title, index = insert_command[0], insert_command[1], int(insert_command[2])
    if lesson_title not in function_list:
        function_list.insert(index, lesson_title)
    return function_list


def remove(function_list, function_command):
    remove_command = function_command.split(":")
    action, lesson_title = remove_command[0], remove_command[1]
    removed = ""
    if lesson_title in function_list:
        removed = lesson_title
        function_list.remove(lesson_title)
    for exercise_local in function_list:
        if removed in exercise_local:
            function_list.remove(exercise_local)
    return function_list


def swap(function_list, function_command):
    swap_command = function_command.split(":")
    action, lesson_title_1, lesson_title_2 = swap_command[0], swap_command[1], swap_command[2]
    index_1 = 0
    index_2 = 0

    ex_bool1 = False
    ex_bool2 = False

    if lesson_title_1 in function_list and lesson_title_2 in function_list:
        index1 = function_list.index(lesson_title_1)
        index2 = function_list.index(lesson_title_2)
        if index1 + 1 in range(len(function_list)):
            if "Exercise" in function_list[index1 + 1]:
                ex_bool1 = True
        if index2 + 1 in range(len(function_list)):
            if "Exercise" in function_list[index2 + 1]:
                ex_bool2 = True

        function_list[index1], function_list[index2] = function_list[index2], function_list[index1]

        if ex_bool1 and ex_bool2:
            function_list[index1 + 1], function_list[index2 + 1] = function_list[index2 + 1], function_list[index1 + 1]
        elif ex_bool1 and not ex_bool2:
            function_list.insert(index2 + 1, function_list.pop(index1 + 1))
        elif not ex_bool1 and ex_bool2:
            function_list.insert(index1 + 1, function_list.pop(index2 + 1))
    return function_list


def exercise(function_list, function_command):
    exercise_command = function_command.split(":")
    action, lesson_tittle = exercise_command[0], exercise_command[1]
    index_lesson = 0
    if lesson_tittle in function_list:
        if lesson_tittle + "-Exercise" not in function_list:
            for i, n in enumerate(function_list):
                if n == lesson_tittle:
                    index = i
                    function_list.insert(index + 1, lesson_tittle + "-Exercise")
    else:
        function_list.append(lesson_tittle)
        function_list.append(lesson_tittle + "-Exercise")
    return function_list


schedule_lessons = [lesson for lesson in input().split(", ")]

while True:
    command = input()
    if command.startswith("course start"):
        break

    elif command.startswith("Add"):
        schedule_lessons = add(schedule_lessons, command)

    elif command.startswith("Insert"):
        schedule_lessons = insert(schedule_lessons, command)

    elif command.startswith("Remove"):
        schedule_lessons = remove(schedule_lessons, command)

    elif command.startswith("Swap"):
        schedule_lessons = swap(schedule_lessons, command)

    elif command.startswith("Exercise"):
        schedule_lessons = exercise(schedule_lessons, command)

for index, lesson in enumerate(schedule_lessons):
    print(f"{index + 1}.{lesson}")