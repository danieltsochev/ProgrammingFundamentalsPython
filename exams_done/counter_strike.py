initial_energy = int(input())

won_battles = 0

is_end_of_battle = False

while True:
    command = input()

    if command == "End of battle":
        is_end_of_battle = True
        break

    distance = int(command)

    if distance > initial_energy:
        print(f"Not enough energy! Game ends with {won_battles} won battles and {initial_energy} energy")
        break

    if initial_energy >= distance:
        initial_energy -= distance
        won_battles += 1
    if won_battles % 3 == 0:
        initial_energy += won_battles

if is_end_of_battle:
    print(f"Won battles: {won_battles}. Energy left: {initial_energy}")