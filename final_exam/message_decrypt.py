import re


def decrypter(message):
    digits = []
    char_list = []

    for element in message:
        digits.append(element[2])
        digits.append(element[3])
        digits.append(element[4])

    for element1 in digits:
        dgt = []
        for e in element1:
            if e.isdigit():
                dgt.append(e)
        char_list.append(dgt)
    decrypt_list = []

    for element2 in char_list:
        result = ""
        decrypt_message = ""
        for element3 in element2:
            result += element3
        decrypt_message += chr(int(result))
        decrypt_list.append(decrypt_message)
    print(f"{message[0][1]}: {''.join(decrypt_list)}")
    return message


messages_count = int(input())

regex = r"^([$%])([A-Z][a-z]{2,})\1: ([\[0-9]+\]\|)([\[0-9]+\]\|)([\[0-9]+\]\|)$"

for iteration in range(messages_count):
    current_message = input()
    char_list = []
    match_message = re.findall(regex, current_message)
    if match_message:
        decrypter(match_message)
    else:
        print("Valid message not found!")
