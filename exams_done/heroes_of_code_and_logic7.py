def cast_spell(function_dict, function_command):
    cs_command = function_command.split(" - ")
    action, hero, mp_needed, spell_name = cs_command[0], cs_command[1], int(cs_command[2]), cs_command[3]
    if function_dict[hero][1] >= mp_needed:
        function_dict[hero][1] -= mp_needed
        print(f"{hero} has successfully cast {spell_name} and now has {function_dict[hero][1]} MP!")
    else:
        print(f"{hero} does not have enough MP to cast {spell_name}!")
    return function_dict


def take_damage(function_dict, function_command):
    td_command = function_command.split(" - ")
    action, hero, damage, attacker = td_command[0], td_command[1], int(td_command[2]), td_command[3]
    function_dict[hero][0] -= damage
    if function_dict[hero][0] > 0:
        print(f"{hero} was hit for {damage} HP by {attacker} and now has {function_dict[hero][0]} HP left!")
    else:
        print(f"{hero} has been killed by {attacker}!")
        del function_dict[hero]
    return function_dict


def recharge(function_dict, function_command):
    recharge_command = function_command.split(" - ")
    action, hero, amount = recharge_command[0], recharge_command[1], int(recharge_command[2])
    max_mp = 200
    if function_dict[hero][1] + amount <= max_mp:
        print(f"{hero} recharged for {amount} MP!")
        function_dict[hero][1] += amount
    else:
        print(f"{hero} recharged for {max_mp - function_dict[hero][1]} MP!")
        function_dict[hero][1] = max_mp
    return function_dict


def heal(function_dict, function_command):
    heal_command = function_command.split(" - ")
    action, hero, amount = heal_command[0], heal_command[1], int(heal_command[2])
    max_hp = 100
    if function_dict[hero][0] + amount <= max_hp:
        print(f"{hero} healed for {amount} HP!")
        function_dict[hero][0] += amount
    else:
        print(f"{hero} healed for {max_hp - function_dict[hero][0]} HP!")
        function_dict[hero][0] = max_hp
    return function_dict


number_of_heroes = int(input())

heroes_dict = {}

for number in range(number_of_heroes):
    current_hero = input().split()
    hero_name, hp, mp = current_hero[0], int(current_hero[1]), int(current_hero[2])
    heroes_dict[hero_name] = [hp, mp]

while True:
    command = input()
    if command.startswith("End"):
        break

    elif command.startswith("CastSpell"):
        heroes_dict = cast_spell(heroes_dict, command)

    elif command.startswith("TakeDamage"):
        heroes_dict = take_damage(heroes_dict, command)

    elif command.startswith("Recharge"):
        heroes_dict = recharge(heroes_dict, command)

    elif command.startswith("Heal"):
        heroes_dict = heal(heroes_dict, command)


for hero, info in heroes_dict.items():
    print(hero)
    print(f"HP: {info[0]}")
    print(f"MP: {info[1]}")