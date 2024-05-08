def play(function_list, index_one, index_two):
    if index_one > index_two:
        function_list.pop(index_one)
        function_list.pop(index_two)
    elif index_two > index_one:
        function_list.pop(index_two)
        function_list.pop(index_one)
    return function_list


def cheat(function_list, function_counter):
    mid_index = int(len(function_list) / 2)
    function_list.insert(mid_index, str(-function_counter) + "a")
    function_list.insert(mid_index, str(-function_counter) + "a")
    return function_list


elements = [element for element in input().split()]

moves_counter = 0

while True:
    command = input()
    if command == "end":
        break

    if len(elements) <= 0:
        continue

    indexes = command.split()
    index1, index2 = int(indexes[0]), int(indexes[1])
    moves_counter += 1
    if index1 == index2:
        print("Invalid input! Adding additional elements to the board")
        elements = cheat(elements, moves_counter)

    elif index1 < 0 or index2 < 0:
        print("Invalid input! Adding additional elements to the board")
        elements = cheat(elements, moves_counter)

    elif index1 >= len(elements) or index2 >= len(elements):
        print("Invalid input! Adding additional elements to the board")
        elements = cheat(elements, moves_counter)

    else:
        if elements[index1] == elements[index2]:
            print(f"Congrats! You have found matching elements - {elements[index1]}!")
            elements = play(elements, index1, index2)
        else:
            print("Try again!")


if len(elements) <= 0:
    print(f"You have won in {moves_counter} turns!")
else:
    print("Sorry you lose :(")
    print(" ".join(elements))


