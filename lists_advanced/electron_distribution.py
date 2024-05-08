number_of_electrons = int(input())

position_of_shell = 0
max_value = 0
shells = []

for index in range(number_of_electrons):
    position_of_shell += 1
    max_value = 2 * position_of_shell ** 2

    if max_value <= number_of_electrons:
        shells.append(max_value)
        number_of_electrons -= max_value
        if number_of_electrons <= 0:
            break
    if max_value > number_of_electrons > 0:
        shells.append(number_of_electrons)
        number_of_electrons = 0

print(shells)