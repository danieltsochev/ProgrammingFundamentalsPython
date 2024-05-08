def potion(blood, amount):
    if blood + amount >= 100:
        print(f"You healed for {100 - blood} hp.")
    else:
        print(f"You healed for {amount} hp.")
    if blood + amount > 100:
        blood = 100
    else:
        blood += amount
    print(f"Current health: {blood} hp.")
    return blood


def chest(coins, amount):
    print(f"You found {amount} bitcoins.")
    coins += amount
    return coins


def attack(enemy, amount,  blood,):
    if blood > amount:
        print(f"You slayed {enemy}.")
        blood -= amount
    else:
        print(f"You died! Killed by {enemy}.")
        blood = 0
    return blood


current_health = 100
bitcoin = 0
room_counter = 0
text = input().split("|")

for element in text:
    room_counter += 1
    room = element.split()
    action, number = room[0], int(room[1])

    if action == "potion":
        current_health = potion(current_health, number)

    elif action == "chest":
        bitcoin = chest(bitcoin, number)

    else:
        current_health = attack(action, number, current_health)
        if current_health <= 0:
            break

if current_health <= 0:
    print(f"Best room: {room_counter}")
else:
    print("You've made it!")
    print(f"Bitcoins: {bitcoin}")
    print(f"Health: {current_health}")
