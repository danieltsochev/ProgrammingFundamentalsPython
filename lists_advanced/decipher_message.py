def deciphering_of_message(function_message):
    for word in function_message:

        basic_list = []
        numbers_as_string = []
        secret_string = []

        for letter in word:
            basic_list.append(letter)

            if letter.isdigit():
                numbers_as_string.append(letter)

            elif letter.isalpha():
                secret_string.append(letter)

        numbers_as_digit = int("".join(numbers_as_string))
        secret_letters = chr(numbers_as_digit)
        secret_string.insert(0, secret_letters)
        secret_string[-1], secret_string[1] = secret_string[1], secret_string[-1]
        secret_message = "".join(secret_string)

        print(secret_message, end=" ")


secret_message_in_put = [word for word in input().split()]

deciphering_of_message(secret_message_in_put)