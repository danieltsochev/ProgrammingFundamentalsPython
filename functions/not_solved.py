def is_even(num):
    if num % 2 == 0:
        return num


numbers_as_string = input().split()
numbers_as_digit = []
for number in numbers_as_string:
    numbers_as_digit.append(int(number))
result = list(filter(is_even, numbers_as_digit))

print(result)