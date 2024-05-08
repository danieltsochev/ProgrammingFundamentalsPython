def moving(text, commands):
    action, letter_count = commands[0], int(commands[1])
    new_text = text[letter_count:] + text[:letter_count]
    return new_text


def inserting(text, commands):
    action, index, value = commands[0], int(commands[1]), commands[2]
    new_text = text[:index] + value + text[index:]
    return new_text


def changing(text, commands):
    action, substring, replacement = commands[0], commands[1], commands[2]
    new_text = text.replace(substring, replacement)
    return new_text


message = input()

new_message = ""

while True:
    command = input()
    if "Decode" in command:
        break

    elif "Move" in command:
        command = command.split("|")
        new_message = moving(message, command)
        message = new_message

    elif "Insert" in command:
        command = command.split("|")
        new_message = inserting(message, command)
        message = new_message

    elif "ChangeAll" in command:
        command = command.split("|")
        new_message = changing(message, command)
        message = new_message


print(f"The decrypted message is: {message}")