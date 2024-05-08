import re

food_info = input()

need_pattern = r"([#|])([A-z]+\s\b[A-z]+|[A-z]+)\1(\d{2}\/\d{2}\/\d{2})\1(\d+)\1"

valid_product_info = re.findall(need_pattern, food_info)

calories = 0

for calorie_in_product in valid_product_info:
    calories += int(calorie_in_product[3])

print(f"You have food to last you for: {int(calories / 2000)} days!")
for product in valid_product_info:
    print(f"Item: {product[1]}, Best before: {product[2]}, Nutrition: {product[3]}")


