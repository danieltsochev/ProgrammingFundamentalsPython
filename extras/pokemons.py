pokemons = [int(pokemon) for pokemon in input().split()]

sum_of_removed = 0
last_removed = 0

while pokemons:
    index = int(input())

    if index < 0:
        last_removed = pokemons[0]
        sum_of_removed += last_removed
        pokemons.pop(0)
        pokemons.insert(0, pokemons[-1])
        pokemons.pop(-1)
        for index in range(len(pokemons)):
            if pokemons[index] <= last_removed:
                pokemons[index] = pokemons[index] + last_removed
            else:
                pokemons[index] = pokemons[index] - last_removed
    elif index >= len(pokemons):
        last_removed = pokemons[-1]
        sum_of_removed += last_removed
        pokemons.pop(-1)
        pokemons.insert(-1, pokemons[0])
        pokemons.pop(-1)
        for index in range(len(pokemons)):
            if pokemons[index] <= last_removed:
                pokemons[index] = pokemons[index] + last_removed
            else:
                pokemons[index] = pokemons[index] - last_removed

    else:
        last_removed = pokemons[index]
        sum_of_removed += last_removed
        pokemons.pop(index)
        for index in range(len(pokemons)):
            if pokemons[index] <= last_removed:
                pokemons[index] = pokemons[index] + last_removed
            else:
                pokemons[index] = pokemons[index] - last_removed
    print(last_removed)
    print(pokemons)
print(sum_of_removed)







