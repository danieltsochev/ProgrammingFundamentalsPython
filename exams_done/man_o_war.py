def fire(ship_war, function_command):
    fire_command = function_command.split()
    action, index, damage = fire_command[0], int(fire_command[1]), int(fire_command[2])
    if index >= 0 and index < len(ship_war):
        ship_war[index] -= damage
    return ship_war


def defend(ship_pirate, function_command):
    defend_command = function_command.split()
    action = defend_command[0]
    start_i = int(defend_command[1])
    end_i = int(defend_command[2])
    damage = int(defend_command[3])
    if start_i <= end_i and start_i >= 0 and start_i < len(ship_pirate) and end_i < len(ship_pirate):
        for section in range(start_i, end_i + 1):
            ship_pirate[section] -= damage
    return ship_pirate


def repair(ship_pirate, function_command, health_max):
    repair_command = function_command.split()
    action, index, health = repair_command[0], int(repair_command[1]), int(repair_command[2])
    if index >= 0 and index < len(ship_pirate):
        ship_pirate[index] += health
        if ship_pirate[index] > health_max:
            ship_pirate[index] = health_max
    return ship_pirate


def status(ship_pirate, health_max):
    damage_for_repair = health_max * 0.20
    section_count = 0
    for section in ship_pirate:
        if section < damage_for_repair:
            section_count += 1
    return f"{section_count} sections need repair."


pirate_ship = [int(section) for section in input().split(">")]
war_ship = [int(section) for section in input().split(">")]

max_health_capacity = int(input())

section_live = True

while True:

    command = input()

    if command == "Retire":
        break

    elif "Fire" in command:
        war_ship = fire(war_ship, command)
        for section in war_ship:
            if section <= 0:
                section_live = False
        if not section_live:
            print("You won! The enemy ship has sunken.")
            break

    elif "Defend" in command:
        pirate_ship = defend(pirate_ship, command)
        for section in pirate_ship:
            if section <= 0:
                section_live = False
        if not section_live:
            print("You lost! The pirate ship has sunken.")
            break

    elif "Repair" in command:
        pirate_ship = repair(pirate_ship, command, max_health_capacity)

    elif "Status" in command:
        print(status(pirate_ship, max_health_capacity))

if section_live:
    print(f"Pirate ship status: {sum(pirate_ship)}")
    print(f"Warship status: {sum(war_ship)}")