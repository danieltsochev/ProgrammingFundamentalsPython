def take_odd(function_text):
    reset_text = ""
    for index, character in enumerate(function_text):
        if index % 2 != 0:
            reset_text += character
    return reset_text


def cut(function_text, function_command):
    cut_command = function_command.split()
    action, start_index, length = cut_command[0], int(cut_command[1]), int(cut_command[2])
    final_index = start_index + length
    first_part = function_text[:start_index]
    second_part = function_text[final_index:]
    reset_text = first_part + second_part
    return reset_text


def substitute(function_text, function_command):
    substitute_command = function_command.split()
    action, substring, substitute_element = substitute_command[0], substitute_command[1], substitute_command[2]
    reset_text = ""
    if substring in function_text:
        reset_text = function_text.replace(substring, substitute_element)
        print(reset_text)
    else:
        reset_text = function_text
        print("Nothing to replace!")
    return reset_text


text = input()

while True:
    command = input()
    if command == "Done":
        break

    elif "TakeOdd" in command:
        text = take_odd(text)
        print(text)

    elif "Cut" in command:
        text = cut(text, command)
        print(text)

    elif "Substitute" in command:
        text = substitute(text, command)


print(f"Your password is: {text}")
