products = {}

while True:
    data = input().split()

    if data[0] == "buy":
        break

    name, price, quantity = data[0], float(data[1]), int(data[2])

    if name not in products.keys():
        products[name] = [price, quantity]

    else:
        products[name][0] = price
        products[name][1] += quantity

for key, value in products.items():
    total_price = value[0] * value[1]
    print(f"{key} -> {total_price:.2f}")