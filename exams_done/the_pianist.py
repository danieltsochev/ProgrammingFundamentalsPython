def add(function_dict, function_command):
    add_command = function_command.split("|")
    action, piece_func, composer_funk, key_func = add_command[0], add_command[1], add_command[2], add_command[3]
    if piece_func not in function_dict.keys():
        function_dict[piece_func] = [composer_funk, key_func]
        print(f"{piece_func} by {composer_funk} in {key_func} added to the collection!")
    else:
        print(f"{piece_func} is already in the collection!")
    return function_dict


def remove(function_dict, function_command):
    remove_command = function_command.split("|")
    action, piece_func = remove_command[0], remove_command[1]
    if piece_func in function_dict.keys():
        print(f"Successfully removed {piece_func}!")
        del function_dict[piece_func]
    else:
        print(f"Invalid operation! {piece_func} does not exist in the collection.")
    return function_dict


def change_key(function_dict, function_command):
    change_key_command = function_command.split("|")
    action, piece_func, new_key = change_key_command[0], change_key_command[1], change_key_command[2]
    if piece_func in function_dict.keys():
        function_dict[piece_func][1] = new_key
        print(f"Changed the key of {piece_func} to {new_key}!")
    else:
        print(f"Invalid operation! {piece_func} does not exist in the collection.")
    return function_dict


number_of_pieces = int(input())

pieces_dict = {}

for number in range(number_of_pieces):
    current_piece = input().split("|")
    piece, composer, key = current_piece[0], current_piece[1], current_piece[2]
    pieces_dict[piece] = [composer, key]

while True:
    command = input()
    if command.startswith("Stop"):
        break

    elif command.startswith("Add"):
        pieces_dict = add(pieces_dict, command)

    elif command.startswith("Remove"):
        pieces_dict = remove(pieces_dict, command)

    elif command.startswith("ChangeKey"):
        pieces_dict = change_key(pieces_dict, command)

for key, value in pieces_dict.items():
    print(f"{key} -> Composer: {value[0]}, Key: {value[1]}")