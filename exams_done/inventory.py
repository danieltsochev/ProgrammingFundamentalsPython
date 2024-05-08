def collect(function_list, function_command):
    collect_command = function_command.split(" - ")
    action, item = collect_command[0], collect_command[1]
    if item not in function_list:
        function_list.append(item)
    return function_list


def drop(function_list, function_command):
    drop_command = function_command.split(" - ")
    action, item = drop_command[0], drop_command[1]
    if item in function_list:
        function_list.remove(item)
    return function_list


def combine(function_list, function_command):
    combine_command = function_command.split(" - ")
    action, two_items = combine_command[0], combine_command[1]
    items_unpack = two_items.split(":")
    old_item, new_item = items_unpack[0], items_unpack[1]
    for index, element in enumerate(function_list):
        if element == old_item:
            function_list.insert(index + 1, new_item)
    return function_list


def renew(function_list, function_command):
    renew_command = function_command.split(" - ")
    action, item = renew_command[0], renew_command[1]
    if item in function_list:
        function_list.remove(item)
        function_list.append(item)
    return function_list


items = [item for item in input().split(", ")]

while True:
    command = input()

    if command.startswith("Craft!"):
        break

    elif command.startswith("Collect"):
        items = collect(items, command)

    elif command.startswith("Drop"):
        items = drop(items, command)

    elif command.startswith("Combine Items"):
        items = combine(items, command)

    elif command.startswith("Renew"):
        items = renew(items, command)

print(", ".join(items))