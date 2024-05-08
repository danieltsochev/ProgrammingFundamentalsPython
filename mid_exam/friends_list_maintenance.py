def blacklist(function_list, function_command):
    blacklist_command = function_command.split()
    action, name = blacklist_command[0], blacklist_command[1]
    changer_name = "Blacklisted"
    if name in function_list:
        for i, n in enumerate(function_list):
            if n == name:
                function_list.insert(i, changer_name)
                print(f"{name} was blacklisted.")
                function_list.remove(n)
    else:
        print(f"{name} was not found.")
    return function_list


def error(function_list, function_command):
    error_command = function_command.split()
    action, index = error_command[0], int(error_command[1])
    lost_name = "Lost"
    if 0 <= index < len(function_list):
        if function_list[index] != "Blacklisted" and function_list[index] != "Lost":
            print(f"{function_list[index]} was lost due to an error.")
            function_list.pop(index)
            function_list.insert(index, lost_name)
    return function_list


def change(function_list, function_command):
    change_command = function_command.split()
    action, index, new_name = change_command[0], int(change_command[1]), change_command[2]
    if 0 <= index < len(function_list):
        print(f"{function_list[index]} changed his username to {new_name}.")
        function_list.pop(index)
        function_list.insert(index, new_name)
    return function_list


friends = [friend for friend in input().split(", ")]

while True:
    command = input()
    if command == "Report":
        break

    elif command.startswith("Blacklist"):
        friends = blacklist(friends, command)

    elif command.startswith("Error"):
        friends = error(friends, command)

    elif command.startswith("Change"):
        friends = change(friends, command)

block = 0
lost = 0

for element in friends:
    if element == "Blacklisted":
        block += 1
    elif element == "Lost":
        lost += 1


print(f"Blacklisted names: {block}")
print(f"Lost names: {lost}")
print(" ".join(friends))