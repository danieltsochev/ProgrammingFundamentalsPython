def add_stop(function_text, function_command):
    adding_command = function_command.split(":")
    action, index, stop = adding_command[0], int(adding_command[1]), adding_command[2]
    reset_text = ""
    if index >= 0 and index < len(function_text):
        first_part = function_text[:index]
        second_part = function_text[index:]
        reset_text = first_part + stop + second_part
        print(reset_text)
    else:
        reset_text = function_text
        print(reset_text)
    return reset_text


def removing(function_text, function_command):
    removing_command = function_command.split(":")
    action, start_index, end_index = removing_command[0], int(removing_command[1]), int(removing_command[2])
    reset_text = ""
    if start_index >= 0 and start_index < len(function_text) and end_index >= 0 and end_index < len(function_text):
        first_part = function_text[:start_index]
        second_part = function_text[end_index + 1:]
        reset_text = first_part + second_part
        print(reset_text)
    else:
        reset_text = function_text
        print(reset_text)
    return reset_text


def switching(function_text, function_command):
    switching_command = function_command.split(":")
    action, old_stop, new_stop = switching_command[0], switching_command[1], switching_command[2]
    reset_text = ""
    if old_stop in function_text:
        reset_text = function_text.replace(old_stop, new_stop)
        print(reset_text)
    else:
        reset_text = function_text
        print(reset_text)
    return reset_text


destinations = input()

while True:
    command = input()

    if command == "Travel":
        break

    elif "Add Stop" in command:
        destinations = add_stop(destinations, command)

    elif "Remove Stop" in command:
        destinations = removing(destinations, command)

    elif "Switch" in command:
        destinations = switching(destinations, command)

print(f"Ready for world tour! Planned stops: {destinations}")