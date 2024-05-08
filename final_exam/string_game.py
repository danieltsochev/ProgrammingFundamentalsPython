data_string = input()
new_string = ""
while True:
    command = input().split()

    if "Done" in command:
        break

    elif "Change" in command:
        if command[1] in data_string:
            new_string = data_string.replace(command[1], command[2])
            data_string = new_string
            print(data_string)

    elif "Includes" in command:
        if command[1] in data_string:
            print("True")
        else:
            print("False")

    elif "End" in command:
        if data_string.endswith(command[1]):
            print("True")
        else:
            print("False")

    elif "Uppercase" in command:
        data_string = data_string.upper()
        print(data_string)

    elif "FindIndex" in command:
        if command[1] in data_string:
            print(data_string.find(command[1]))

    elif "Cut" in command:
        start_index = int(command[1])
        count = int(command[2])
        print(data_string[start_index:start_index + count])

