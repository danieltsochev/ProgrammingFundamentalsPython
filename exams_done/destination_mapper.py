import re

text = input()

regex = r"(\={1}|\/{1})([A-Z][A-z]{2,})\1"

valid_destinations = re.findall(regex, text)

destinations_list = []

travel_points = 0
if valid_destinations:
    for destination in valid_destinations:
        destinations_list.append(destination[1])

for element in valid_destinations:
    travel_points += len(element[1])

if destinations_list:
    print(f"Destinations: {', '.join(destinations_list)}")
else:
    print("Destinations:")
print(f"Travel Points: {travel_points}")