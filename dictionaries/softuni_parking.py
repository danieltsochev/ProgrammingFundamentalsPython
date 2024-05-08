def registering(function_dict, function_command):
    register_command = function_command.split()
    action, name, plate = register_command[0], register_command[1], register_command[2]
    if name not in function_dict.keys():
        function_dict[name] = plate
        print(f"{name} registered {plate} successfully")
    else:
        print(f"ERROR: already registered with plate number {function_dict[name]}")
    return function_dict


def unregistering(function_dict, function_command):
    leaving_command = function_command.split()
    action, name = leaving_command[0], leaving_command[1]
    if name in function_dict.keys():
        print(f"{name} unregistered successfully")
        del function_dict[name]
    else:
        print(f"ERROR: user {name} not found")
    return function_dict


parking_info = {}

number_of_commands = int(input())

for iteration in range(number_of_commands):
    current_info = input()
    if current_info.startswith("register"):
        parking_info = registering(parking_info, current_info)
    elif current_info.startswith("unregister"):
        parking_info = unregistering(parking_info, current_info)

for name, plate in parking_info.items():
    print(f"{name} => {plate}")