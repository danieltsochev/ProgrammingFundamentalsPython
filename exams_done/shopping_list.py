def urgent(function_list, function_command):
    split_command = function_command.split()
    action, item = split_command[0], split_command[1]
    if item not in function_list:
        function_list.insert(0, item)
    return function_list


def unnecessary(function_list, function_command):
    split_command = function_command.split()
    action, item = split_command[0], split_command[1]
    if item in function_list:
        function_list.remove(item)
    return function_list


def correct(function_list, function_command):
    split_command = function_command.split()
    action, old_item, new_item = split_command[0], split_command[1], split_command[2]
    index_needed = 0
    for index, item in enumerate(function_list):
        if old_item == item:
            index_needed = index
            function_list.remove(old_item)
            function_list.insert(index_needed, new_item)
    return function_list


def rearrange(function_list, function_command):
    split_command = function_command.split()
    action, item = split_command[0], split_command[1]
    if item in function_list:
        function_list.remove(item)
        function_list.append(item)
    return function_list


groceries_list = [item for item in input().split("!")]

while True:
    command = input()

    if command == "Go Shopping!":
        break

    elif "Urgent" in command:
        groceries_list = urgent(groceries_list, command)

    elif "Unnecessary" in command:
        groceries_list = unnecessary(groceries_list, command)

    elif "Correct" in command:
        groceries_list = correct(groceries_list, command)

    elif "Rearrange" in command:
        groceries_list = rearrange(groceries_list, command)

print(", ".join(groceries_list))