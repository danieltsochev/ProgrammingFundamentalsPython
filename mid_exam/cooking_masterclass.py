from math import ceil

budget = float(input())
students = int(input())
flour_price = float(input())
egg_price = float(input())
apron_price = float(input())

money_for_flour = 0
five_counter = 0
total_flour = 0
for student in range(1, students + 1):
    money_for_flour += flour_price
    if student % 5 == 0:
        five_counter += 1
total_flour = money_for_flour - (five_counter * flour_price)

money_for_eggs = (students * 10) * egg_price

money_for_aprons = ceil(students * 1.20) * apron_price

all_money_needed = total_flour + money_for_eggs + money_for_aprons

if budget >= all_money_needed:
    print(f"Items purchased for {all_money_needed:.2f}$.")
else:
    print(f"{all_money_needed - budget:.2f}$ more needed.")
