MAX_SIZE = 4

people = int(input())
cabins = [int(cabin) for cabin in input().split()]


for index in range(len(cabins)):
    free_space = MAX_SIZE - cabins[index]

    if people >= free_space:
        cabins[index] += free_space
    else:
        cabins[index] += people

    people -= free_space

    if people <= 0 and (index != len(cabins) - 1 or cabins[index] < MAX_SIZE):
        print("The lift has empty spots!")
        break

else:
    if people > 0:
        print(f"There isn't enough space! {people} people in queue!")

print(*cabins)