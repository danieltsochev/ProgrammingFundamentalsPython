def length(function_password):
    if len(function_password) < 6 or len(function_password) > 10:
        print(f"Password must be between 6 and 10 characters")
        return False
    return True


def simbols(function_password):
    if not function_password.isalnum():
        print("Password must consist only of letters and digits")
        return False
    return True


def digits(function_password):
    digit_counter = 0
    for element in function_password:
        if element.isdigit():
            digit_counter += 1
    if digit_counter < 2:
        print("Password must have at least 2 digits")
        return False
    return True


password = input()
is_pass_valid = [length(password), simbols(password), digits(password)]

if all(is_pass_valid):
    print("Password is valid")