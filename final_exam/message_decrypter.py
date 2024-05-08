import re

number_of_inputs = int(input())

my_list = []

matches = ""

pattern = r"(\$|%)([A-Za-z]{3,})\1(\:\s{1})(\[[0-9]+\]\|)(\[[0-9]+\]\|)(\[[0-9]+\]\|)"

for iteration in range(number_of_inputs):
    message = input()
    matches = re.findall(pattern, message)
    if matches:
        print(matches)
    else:
        print("no matches")
