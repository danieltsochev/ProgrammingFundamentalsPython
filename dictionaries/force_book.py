def side_user(function_dict, function_command):
    side_user_command = function_command.split(" | ")
    force_side, force_user = side_user_command[0], side_user_command[1]
    list_with_names = []

    for value in function_dict.values():
        for name in value:
            list_with_names.append(name)
    if force_user not in list_with_names and force_side not in function_dict.keys():
        function_dict[force_side] = [force_user]

    elif force_user not in list_with_names and force_side in function_dict.keys():
        function_dict[force_side].append(force_user)
    return function_dict


def user_side(function_dict, function_command):
    user_side_command = function_command.split(" -> ")
    force_user, force_side = user_side_command[0], user_side_command[1]
    list_with_names = []

    for value in function_dict.values():
        for name in value:
            list_with_names.append(name)
    if force_user not in list_with_names and force_side not in function_dict.keys():
        function_dict[force_side] = [force_user]
    elif force_user in list_with_names and force_side in function_dict.keys():
        for value in function_dict.values():
            for name in value:
                if name == force_user:
                    value.remove(name)
        function_dict[force_side].append(force_user)
    elif force_user not in list_with_names and force_side in function_dict.keys():
        function_dict[force_side].append(force_user)

    print(f"{force_user} joins the {force_side} side!")
    return function_dict


force_book = {}

while True:
    command = input()
    if command == "Lumpawaroo":
        break

    elif "|" in command:
        force_book = side_user(force_book, command)

    elif "->" in command:
        force_book = user_side(force_book, command)


for side, members in force_book.items():
    if len(members) > 0:
        print(f"Side: {side}, Members: {len(members)}")
        for name in members:
            if len(members) > 0:
                print(f"! {name}")
