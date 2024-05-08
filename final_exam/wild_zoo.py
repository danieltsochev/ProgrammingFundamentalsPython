def add(animal_dict, animal_info):
    add_command = animal_info.split("-")
    name, food, area = add_command[0], int(add_command[1]), add_command[2]
    if name not in animal_dict.keys():
        animal_dict[name] = [food, area]
    else:
        animal_dict[name][0] += food
    return animal_dict


def feed(animal_dict, animal_info):
    feed_command = animal_info.split("-")
    name, food = feed_command[0], int(feed_command[1])
    if name in animal_dict.keys():
        animal_dict[name][0] -= food
        if animal_dict[name][0] <= 0:
            print(f"{name} was successfully fed")
            del animal_dict[name]
    return animal_dict


animals = {}

while True:
    command = input()
    if command == "EndDay":
        break

    command_split = command.split(": ")
    action, animal_data = command_split[0], command_split[1]

    if action == "Add":
        animals = add(animals, animal_data)

    elif action == "Feed":
        animals = feed(animals, animal_data)

area_data = {}

for area in animals.values():
    if area[1] not in area_data.keys():
        area_data[area[1]] = 1
    else:
        area_data[area[1]] += 1


print("Animals:")

for key, value in animals.items():
    print(f"{key} -> {value[0]}g")

print("Areas with hungry animals:")

for key1, value1 in area_data.items():
    print(f"{key1}: {value1}")
