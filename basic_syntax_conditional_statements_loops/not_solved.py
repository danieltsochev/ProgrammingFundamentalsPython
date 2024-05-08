number_of_orders = int(input())

total_price = 0

for orders in range(number_of_orders):

    coffe_price = 0

    price_per_capsule = float(input())
    days = int(input())
    capsule_daily_need = int(input())
    if price_per_capsule <= 0 or days <= 0 or capsule_daily_need <= 0:
        continue

    coffe_price += (days * capsule_daily_need) * price_per_capsule
    total_price += coffe_price

    print(f"The price for the coffee is: ${coffe_price:.2f}")

print(f"Total: ${total_price:.2f}")
