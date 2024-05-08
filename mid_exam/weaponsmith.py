def adding(function_list, commands):
    action, element, index = commands[0], commands[1], int(commands[2])
    if index < len(function_list):
        function_list.insert(index, element)
    return function_list


def removing(function_list, commands):
    action, index = commands[0], int(commands[1])
    if index < len(function_list):
        function_list.pop(index)
    return function_list


def even_check(function_list, commands):
    action, statement = commands[0], commands[1]
    for index in range(len(function_list)):
        if index % 2 == 0:
            print(function_list[index], end=" ")


def odd_check(function_list, commands):
    action, statement = commands[0], commands[1]
    for index in range(len(function_list)):
        if index % 2 != 0:
            print(function_list[index], end=" ")


weapon_parts = input().split("|")

while True:
    command = input().split()

    if "Done" in command:
        print(f"You crafted {''.join(weapon_parts)}!")
        break

    elif "Add" in command:
        command = command
        adding(weapon_parts, command)

    elif "Remove" in command:
        command = command
        removing(weapon_parts, command)

    elif "Even" in command:
        even_check(weapon_parts, command)

    elif "Odd" in command:
        odd_check(weapon_parts, command)
