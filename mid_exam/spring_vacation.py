days_of_trip = int(input())
budget = float(input())
people_count = int(input())
price_fuel_km = float(input())
food_per_person_day = float(input())
room_person_night = float(input())

total_food = (food_per_person_day * people_count) * days_of_trip

accommodations = (room_person_night * people_count) * days_of_trip
if people_count > 10:
    accommodations *= 0.75

total_expenses = 0
total_expenses += total_food
total_expenses += accommodations


for day in range(1, days_of_trip + 1):
    current_destination = float(input())
    total_expenses += current_destination * price_fuel_km



    if day % 3 == 0 or day % 5 == 0:
        total_expenses += (total_expenses * 0.40)

    elif day % 7 == 0:
        total_expenses -= (total_expenses / people_count)

    if budget <= total_expenses:
        break

if budget >= total_expenses:
    print(f"You have reached the destination. You have {budget - total_expenses:.2f}$ budget left.")
else:
    print(f"Not enough money to continue the trip. You need {total_expenses - budget:.2f}$ more.")

