def contains(key_word, command1):
    command_in = command1.split(">>>")
    action, substring = command_in[0], command_in[1]
    if substring in key_word:
        print(f"{key_word} contains {substring}")
    else:
        print("Substring not found!")
    return key_word


def flip(key_word, command1):
    command_in = command1.split(">>>")
    action, upper_lower, start_i, end_i = command_in[0], command_in[1], int(command_in[2]), int(command_in[3])
    if upper_lower == "Upper":
        key_word = key_word.replace(key_word[start_i:end_i], key_word[start_i:end_i].upper(), 1)
    elif upper_lower == "Lower":
        key_word = key_word.replace(key_word[start_i:end_i], key_word[start_i:end_i].lower(), 1)
    print(key_word)
    return key_word


def slice(key_word, command1):
    command_in = command1.split(">>>")
    action, start_i, end_i = command_in[0], int(command_in[1]), int(command_in[2])
    key_word = key_word.replace(key_word[start_i:end_i], "", 1)
    print(key_word)
    return key_word


activation_key = input()

while True:
    command = input()
    if command == "Generate":
        break

    elif command.startswith("Contain"):
        activation_key = contains(activation_key, command)

    elif command.startswith("Flip"):
        activation_key = flip(activation_key, command)

    elif command.startswith("Slice"):
        activation_key = slice(activation_key, command)

print(f"Your activation key is: {activation_key}")