total_price = 0
taxes = 0
customer_type = ""
final_bill = 0
while True:
    type_of_receive = input()
    if type_of_receive == "special":
        customer_type = type_of_receive
        break
    elif type_of_receive == "regular":
        customer_type = type_of_receive
        break

    pc_part_price = float(type_of_receive)

    if pc_part_price < 0:
        print("Invalid price!")

    else:
        total_price += pc_part_price
        taxes += (pc_part_price * 0.20)

if total_price <= 0:
    print("Invalid order!")
    exit()

print("Congratulations you've just bought a new computer!")
print(f"Price without taxes: {total_price:.2f}$")
print(f"Taxes: {taxes:.2f}$")
print("-----------")
if customer_type == "special":
    final_bill = (total_price + taxes) * 0.90
elif customer_type == "regular":
    final_bill = total_price + taxes

print(f"Total price: {final_bill:.2f}$")

