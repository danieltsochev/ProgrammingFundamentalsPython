house_input = input().split("@")
houses = []
for element in house_input:
    houses.append(int(element))

last_jump = 0
not_visited = 0

while True:
    command = input()
    if command == "Love!":
        break

    jumping_command = command.split()
    action, jump = jumping_command[0], int(jumping_command[1])


    if jump >= 0 and jump < len(houses):
        if last_jump + jump < len(houses):
            last_jump = last_jump + jump
            if houses[last_jump] > 0:
                houses[last_jump] -= 2
                if houses[last_jump] == 0:
                    print(f"Place {last_jump} has Valentine's day.")

            else:
                print(f"Place {last_jump} already had Valentine's day.")
        else:
            last_jump = 0
            if houses[last_jump] > 0:
                houses[last_jump] -= 2
                if houses[last_jump] == 0:
                    print(f"Place {last_jump} has Valentine's day.")
            else:
                print(f"Place {last_jump} already had Valentine's day.")

    else:
        last_jump = 0
        if houses[last_jump] > 0:
            houses[last_jump] -= 2
            if houses[last_jump] == 0:
                print(f"Place {last_jump} has Valentine's day.")
        else:
            print(f"Place {last_jump} already had Valentine's day.")

print(f"Cupid's last position was {last_jump}.")

for home in houses:
    if home > 0:
        not_visited += 1

if sum(houses) <= 0:
    print("Mission was successful.")
else:
    print(f"Cupid has failed {not_visited} places.")