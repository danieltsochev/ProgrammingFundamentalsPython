def swap(function_list, function_command):
    swap_command = function_command.split()
    action, index_1, index_2 = swap_command[0], int(swap_command[1]), int(swap_command[2])
    function_list[index_1], function_list[index_2] = function_list[index_2], function_list[index_1]
    return function_list


def multiply(function_list, function_command):
    multiply_command = function_command.split()
    action, index_1, index_2 = multiply_command[0], int(multiply_command[1]), int(multiply_command[2])
    result = function_list[index_1] * function_list[index_2]
    for i in range(len(function_list)):
        function_list.pop(index_1)
        function_list.insert(index_1, result)
    return function_list


def decrease(function_list):
    for index in range(len(function_list)):
        function_list[index] -= 1
    return function_list


def printing(function_list):
    string_array = []
    for number in function_list:
        string_array.append(str(number))
    return ", ".join(string_array)


array = [int(number) for number in input().split()]

while True:
    command = input()
    if command == "end":
        break

    elif command.startswith("swap"):
        array = swap(array, command)

    elif command.startswith("multiply"):
        array = multiply(array, command)

    elif command.startswith("decrease"):
        array = decrease(array)

print(printing(array))