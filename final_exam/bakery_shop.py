bakery = {}
products_sold = 0
while True:
    commands = input().split()

    if commands[0] == "Complete":
        break

    action, quantity, product = commands[0], int(commands[1]), commands[2]

    if action == "Receive":
        if product not in bakery:
            bakery[product] = quantity
        else:
            bakery[product] += quantity

        if quantity <= 0:
            continue

    elif action == "Sell":
        if product not in bakery:
            print(f"You do not have any {product}.")
        else:
            bakery[product] -= quantity
            print(f"You sold {quantity} {product}.")
            products_sold += quantity

for product, quantity in bakery.items():
    if quantity > 0:
        print(f"{product}: {quantity}")

print(f"All sold: {products_sold} goods")

