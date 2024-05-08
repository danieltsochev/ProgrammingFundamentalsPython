def plunder(function_dict, function_command):
    plunder_command = function_command.split("=>")
    action, town, people, gold = plunder_command[0], plunder_command[1], int(plunder_command[2]), int(plunder_command[3])
    if town in function_dict.keys():
        function_dict[town][0] -= people
        function_dict[town][1] -= gold
        print(f"{town} plundered! {gold} gold stolen, {people} citizens killed.")
        if function_dict[town][0] <= 0 or function_dict[town][1] <= 0:
            print(f"{town} has been wiped off the map!")
            del function_dict[town]
    return function_dict


def prosper(function_dict, function_command):
    prosper_command = function_command.split("=>")
    action, town, gold = prosper_command[0], prosper_command[1], int(prosper_command[2])
    if town in function_dict.keys():
        if gold >= 0:
            function_dict[town][1] += gold
            print(f"{gold} gold added to the city treasury. {town} now has {function_dict[town][1]} gold.")
        else:
            print("Gold added cannot be a negative number!")
    return function_dict


pirate_data = {}

while True:
    command = input().split("||")
    if "Sail" in command:
        break

    city, population, gold_of_city = command[0], int(command[1]), int(command[2])

    if city not in pirate_data.keys():
        pirate_data[city] = [population, gold_of_city]
    else:
        pirate_data[city][0] += population
        pirate_data[city][1] += gold_of_city

while True:
    event_command = input()
    if event_command.startswith("End"):
        break

    elif event_command.startswith("Plunder"):
        pirate_data = plunder(pirate_data, event_command)

    elif event_command.startswith("Prosper"):
        pirate_data = prosper(pirate_data, event_command)


if pirate_data:
    print(f"Ahoy, Captain! There are {len(pirate_data.keys())} wealthy settlements to go to:")
    for place, information in pirate_data.items():
        print(f"{place} -> Population: {information[0]} citizens, Gold: {information[1]} kg")
else:
    print(f"Ahoy, Captain! All targets have been plundered and destroyed!")