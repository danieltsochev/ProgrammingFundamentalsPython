email_string = input()
new_string = ""
while True:
    command = input()
    if "Complete" in command:
        break

    elif "Make Upper" in command:
        new_string = email_string.upper()
        email_string = new_string
        print(new_string)

    elif "Make Lower" in command:
        new_string = email_string.lower()
        email_string = new_string
        print(new_string)

    elif "GetDomain" in command:
        command = command.split()
        action, count = command[0], int(command[1])
        new_string = email_string[-count:]
        print(new_string)

    elif "GetUsername" in command:
        if "@" not  in email_string:
            print(f"The email {email_string} doesn't contain the @ symbol.")
        else:

            username = email_string.split("@")
            print(username[0])


    elif "Replace" in command:
        command = command.split()
        action1, char = command[0], command[1]
        email_string = email_string.replace(char, "-")
        print(email_string)

    elif "Encrypt" in command:
        for element in email_string:
            print(ord(element), end=" ")

