def rate(function_dict, function_command):
    rate_command = function_command.split(" - ")
    plant, rating = rate_command[0], int(rate_command[1])
    if plant in function_dict.keys():
        function_dict[plant][1].append(rating)
    else:
        print("error")
    return function_dict


def update(function_dict, function_command):
    update_command = function_command.split(" - ")
    plant, new_rarity = update_command[0], int(update_command[1])
    if plant in function_dict.keys():
        function_dict[plant][0] = new_rarity
    else:
        print("error")
    return function_dict


def reset(function_dict, function_command):
    plant = function_command
    if plant in function_dict.keys():
        function_dict[plant][1] = []
    else:
        print("error")
    return function_dict


def rating_problem(function_dict):
    for key, value in function_dict.items():
        if len(value[1]) <= 0:
            value[1] = 0
        else:
            value[1] = (sum(value[1]) / len(value[1]))
    return function_dict


number_of_plants = int(input())
plant_book = {}

for number in range(number_of_plants):
    current_plant = input().split("<->")
    plant_name, plant_rarity = current_plant[0], int(current_plant[1])
    plant_book[plant_name] = [plant_rarity, []]

while True:
    command = input()
    if command == "Exhibition":
        break

    information = command.split(": ")
    action, plant_info = information[0], information[1]

    if action == "Rate":
        plant_book = rate(plant_book, plant_info)

    elif action == "Update":
        plant_book = update(plant_book, plant_info)

    elif action == "Reset":
        plant_book = reset(plant_book, plant_info)

plant_book = rating_problem(plant_book)

print("Plants for the exhibition:")
for plant_type, information_plant in plant_book.items():
    print(f"- {plant_type}; Rarity: {information_plant[0]}; Rating: {information_plant[1]:.2f}")