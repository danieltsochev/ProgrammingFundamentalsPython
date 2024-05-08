import re


def validate_travel_destination(data_function):

    pattern = r"(\:{2,}|\*{2,})([A-Z][a-z]{2,})\1"
    travel_points = 0
    valid_destination = []
    result = re.finditer(pattern, data_function)


    for current_destination in result:
        valid_destination.append(current_destination.group(2))
        travel_points += len(current_destination.group(2))
    print(f"Destinations: {', '.join(valid_destination)}\nTravel Points: {travel_points}")


data = input()
validate_travel_destination(data)
