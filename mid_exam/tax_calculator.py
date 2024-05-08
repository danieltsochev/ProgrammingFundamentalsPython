def family(function_family):
    counter = 0
    for element in function_family:
        inside = element.split()
        declines = int(inside[1]) * 5
        increases = (int(inside[2]) // 3000) * 12
        result = 50 - declines + increases
        counter += 1
        if counter >= len(function_family):
            return result


def heavy_duty(function_heavy_duty):
    counter = 0
    for element in function_heavy_duty:
        inside = element.split()
        declines = int(inside[1]) * 8
        increases = (int(inside[2]) // 9000) * 14
        result = 80 - declines + increases
        counter += 1
        if counter >= len(function_heavy_duty):
            return result


def sports(function_sport):
    counter = 0
    for element in function_sport:
        inside = element.split()
        declines = int(inside[1]) * 9
        increases = (int(inside[2]) // 2000) * 18
        result = 100 - declines + increases
        counter += 1
        if counter >= len(function_sport):
            return result


cars_list = [car for car in input().split(">>")]

family_car = []
heavy_duty_car = []
sports_car = []
total_coast = 0

for car in cars_list:
    if "family" in car:
        family_car.append(car)
        total_coast += int(family(family_car))
        print(f"A family car will pay {family(family_car):.2f} euros in taxes.")

    elif "heavyDuty" in car:
        heavy_duty_car.append(car)
        total_coast += int(heavy_duty(heavy_duty_car))
        print(f"A heavyDuty car will pay {heavy_duty(heavy_duty_car):.2f} euros in taxes.")

    elif "sports" in car:
        sports_car.append(car)
        total_coast += int(sports(sports_car))
        print(f"A sports car will pay {sports(sports_car):.2f} euros in taxes.")

    else:
        print("Invalid car type.")

print(f"The National Revenue Agency will collect {total_coast:.2f} euros in taxes.")

