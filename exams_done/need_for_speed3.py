def drive(f_dict, f_command):
    d_command = f_command.split(" : ")
    action, f_car, f_distance, f_fuel = d_command[0], d_command[1], int(d_command[2]), int(d_command[3])
    if f_dict[f_car][1] >= f_fuel:
        f_dict[f_car][0] += f_distance
        f_dict[f_car][1] -= f_fuel
        print(f"{f_car} driven for {f_distance} kilometers. {f_fuel} liters of fuel consumed.")
    else:
        print("Not enough fuel to make that ride")
    if f_dict[f_car][0] >= 100000:
        print(f"Time to sell the {f_car}!")
        del f_dict[f_car]
    return f_dict


def refuel(f_dict, f_command):
    ref_command = f_command.split(" : ")
    action, f_car, f_fuel = ref_command[0], ref_command[1], int(ref_command[2])
    max_tank = 75
    if f_dict[f_car][1] + f_fuel <= max_tank:
        f_dict[f_car][1] += f_fuel
        print(f"{f_car} refueled with {f_fuel} liters")
    else:
        print(f"{f_car} refueled with {max_tank - f_dict[f_car][1]} liters")
        f_dict[f_car][1] = max_tank
    return f_dict


def revert(f_dict, f_command):
    rev_command = f_command.split(" : ")
    action, f_car, f_kilometers = rev_command[0], rev_command[1], int(rev_command[2])
    if f_dict[f_car][0] - f_kilometers >= 10000:
        f_dict[f_car][0] -= f_kilometers
        print(f"{f_car} mileage decreased by {f_kilometers} kilometers")
    else:
        f_dict[f_car][0] = 10000
    return f_dict


garage = {}

n_cars = int(input())

for iteration in range(n_cars):
    current_car = input().split("|")
    car, mileage, fuel = current_car[0], int(current_car[1]), int(current_car[2])
    garage[car] = [mileage, fuel]

while True:
    command = input()
    if command == "Stop":
        break

    elif command.startswith("Drive"):
        garage = drive(garage, command)

    elif command.startswith("Refuel"):
        garage = refuel(garage, command)

    elif command.startswith("Revert"):
        garage = revert(garage, command)

for key, value in garage.items():
    print(f"{key} -> Mileage: {value[0]} kms, Fuel in the tank: {value[1]} lt.")
