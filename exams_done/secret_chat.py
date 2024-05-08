def insert_space(function_string, function_command):
    in_command = function_command.split(":|:")
    action, index = in_command[0], int(in_command[1])
    result = ""
    result = function_string[:index] + " " + function_string[index:]
    print(result)
    return result


def reverse(function_string, function_command):
    in_command = function_command.split(":|:")
    in_command = function_command.split(":|:")
    action, substring = in_command[0], in_command[1]
    mirror_substring = substring[::-1]
    result = ""
    if substring in function_string:
        function_string = function_string.replace(substring, "", 1)
        result = function_string + mirror_substring
        print(result)
    else:
        print("error")
        result = function_string
    return result


def change_all(function_string, function_command):
    in_command = function_command.split(":|:")
    action, substring, replacement = in_command[0], in_command[1], in_command[2]
    result = ""
    if substring in function_string:
        result = function_string.replace(substring, replacement)
        print(result)
    return result


concealed_message = input()

while True:
    command = input()

    if command.startswith("Reveal"):
        break

    elif command.startswith("InsertSpace"):
        concealed_message = insert_space(concealed_message, command)

    elif command.startswith("Reverse"):
        concealed_message = reverse(concealed_message, command)

    elif command.startswith("ChangeAll"):
        concealed_message = change_all(concealed_message, command)

print(f"You have a new text message: {concealed_message}")