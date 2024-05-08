def sum_numbers(first_num, second_num):
    result_add = first_num + second_num
    return result_add


def subtract(result1, third):
    result2 = result1 - third
    return result2


def add_and_subtract(num1, num2, num3):
    sum_numbers(num1, num2)
    result_one = sum_numbers(num1, num2)
    subtract(result_one, third_number)
    return result_one - third_number


first_number = int(input())
second_number = int(input())
third_number = int(input())

print(add_and_subtract(first_number, second_number, third_number))