stocks = input().split()

stock = {}

for i in range(0, len(stocks), 2):
    product = stocks[i]
    quantity = int(stocks[i + 1])
    stock[product] = quantity

searching_stock = input().split()

for product in searching_stock:
    if product in stock:
        print(f"We have {stock[product]} of {product} left")
    else:
        print(f"Sorry, we don't have {product}")