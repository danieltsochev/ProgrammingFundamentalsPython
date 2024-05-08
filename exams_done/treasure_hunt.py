def average_treasure_gain(function_list):
    result = 0
    items = len(function_list)
    sum_length_items = 0
    for element in function_list:
        sum_length_items += len(element)
    result = sum_length_items / items
    return f"Average treasure gain: {result:.2f} pirate credits."


def loot(function_list, function_command):
    loot_command = function_command.split()
    action, items = loot_command[0], loot_command[1:]
    for specific_item in items:
        if specific_item not in function_list:
            function_list.insert(0, specific_item)
    return function_list


def drop(function_list, function_command):
    dropped_element = ""
    drop_command = function_command.split()
    action, index = drop_command[0], int(drop_command[1])
    if 0 <= index < len(function_list):
        dropped_element = function_list[index]
        function_list.pop(index)
        function_list.append(dropped_element)
    return function_list


def steal(function_list, function_command):
    stolen = []
    steal_command = function_command.split()
    action, count = steal_command[0], int(steal_command[1])
    if count < len(function_list):
        for cleaning in range(count):
            stolen.insert(0, function_list[-1])
            function_list.remove(function_list[-1])
    else:
        for cleaning in range(len(function_list)):
            stolen.insert(0, function_list[-1])
            function_list.remove(function_list[-1])
    if len(stolen) > 0:
        print(", ".join(stolen))
    return function_list


treasure_chest = [item for item in input().split("|")]

while True:
    command = input()

    if command.startswith("Yohoho!"):
        break

    elif command.startswith("Loot"):
        treasure_chest = loot(treasure_chest, command)

    elif command.startswith("Drop"):
        treasure_chest = drop(treasure_chest, command)

    elif command.startswith("Steal"):
        treasure_chest = steal(treasure_chest, command)

if len(treasure_chest) <= 0:
    print("Failed treasure hunt.")
else:
    print(average_treasure_gain(treasure_chest))