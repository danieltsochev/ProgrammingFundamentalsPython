def translate(text, function_command):
    translate_command = function_command.split()
    action, char, replacement = translate_command[0], translate_command[1], translate_command[2]
    if char in text:
        text = text.replace(char, replacement)
    print(text)
    return text


def includes(text, function_command):
    includes_command = function_command.split()
    action, substring = includes_command[0], includes_command[1]
    if substring in text:
        print("True")
    else:
        print("False")
    return text


def start(text, function_command):
    start_command = function_command.split()
    action, substring = start_command[0], start_command[1]
    if text.startswith(substring):
        print("True")
    else:
        print("False")
    return text


def lowercase(text, function_command):
    text = text.lower()
    print(text)
    return text


def find_index(text, function_command):
    find_index_command = function_command.split()
    action, char = find_index_command[0], find_index_command[1]
    index_list = []
    if char in text:
        for index in range(len(text)):
            if text[index] == char:
                index_list.append(index)
    if index_list:
        print(max(index_list))
    return text


def remove(text, function_command):
    remove_command = function_command.split()
    action, start_index, count = remove_command[0], int(remove_command[1]), int(remove_command[2])
    if 0 <= start_index < len(text):
        if start_index > 0:
            text = text[:start_index] + text[(start_index + count):]
            print(text)
        else:
            text = text[(start_index + count):]
            print(text)
    return text


text_string = input()

while True:
    command = input()
    if command == "End":
        break

    elif command.startswith("Translate"):
        text_string = translate(text_string, command)

    elif command.startswith("Includes"):
        text_string = includes(text_string, command)

    elif command.startswith("Start"):
        text_string = start(text_string, command)

    elif command.startswith("Lowercase"):
        text_string = lowercase(text_string, command)

    elif command.startswith("FindIndex"):
        text_string = find_index(text_string, command)

    elif command.startswith("Remove"):
        text_string = remove(text_string, command)