def shoot(function_list, function_command):
    shoot_command = function_command.split()
    action, index, power = shoot_command[0], int(shoot_command[1]), int(shoot_command[2])
    if 0 <= index < len(function_list):
        function_list[index] -= power
        if function_list[index] <= 0:
            function_list.pop(index)
    return function_list


def add(function_list, function_command):
    add_command = function_command.split()
    action, index, value = add_command[0], int(add_command[1]), int(add_command[2])
    if 0 <= index < len(function_list):
        function_list.insert(index, value)
    else:
        print("Invalid placement!")
    return function_list


def strike(function_list, function_command):
    strike_command = function_command.split()
    action, index, radius = strike_command[0], int(strike_command[1]), int(strike_command[2])
    start_index = index - radius
    end_index = index + 1
    if start_index >= 0 and end_index < len(function_list):
        for target in function_list[start_index:end_index + 1]:
            function_list.remove(target)
    else:
        print("Strike missed!")
    return function_list


def transformation(function_list):
    transform_list = []
    for target in function_list:
        transform_list.append(str(target))
    return transform_list


targets = [int(target) for target in input().split()]

while True:
    command = input()
    if command == "End":
        break

    elif command.startswith("Shoot"):
        targets = shoot(targets, command)

    elif command.startswith("Add"):
        targets = add(targets, command)

    elif command.startswith("Strike"):
        targets = strike(targets, command)

targets = transformation(targets)

print("|".join(targets))