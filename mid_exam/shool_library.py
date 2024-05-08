def add(function_list, function_command):
    add_command = function_command.split(" | ")
    action, book_name = add_command[0], add_command[1]
    if book_name not in function_list:
        function_list.insert(0, book_name)
    return function_list


def take(function_list, function_command):
    take_command = function_command.split(" | ")
    action, book_name = take_command[0], take_command[1]
    if book_name in function_list:
        function_list.remove(book_name)
    return function_list


def swap(function_list, function_command):
    swap_command = function_command.split(" | ")
    action, book_one, book_two = swap_command[0], swap_command[1], swap_command[2]
    index_one = 0
    index_two = 0
    if book_one in function_list and book_two in function_list:
        index_one = function_list.index(book_one)
        index_two = function_list.index(book_two)
        function_list[index_one], function_list[index_two] = function_list[index_two], function_list[index_one]
    return function_list


def insert(function_list, function_command):
    insert_command = function_command.split(" | ")
    action, book_name = insert_command[0], insert_command[1]
    if book_name not in function_list:
        function_list.append(book_name)
    return function_list


def check(function_list, function_command):
    check_command = function_command.split(" | ")
    action, index = check_command[0], int(check_command[1])
    if 0 <= index < len(function_list):
        print(function_list[index])
    return function_list


shelf_books = [book for book in input().split("&")]

while True:
    command = input()
    if command == "Done":
        break

    elif command.startswith("Add Book"):
        shelf_books = add(shelf_books, command)

    elif command.startswith("Take Book"):
        shelf_books = take(shelf_books, command)

    elif command.startswith("Swap Books"):
        shelf_books = swap(shelf_books, command)

    elif command.startswith("Insert Book"):
        shelf_books = insert(shelf_books, command)

    elif command.startswith("Check Book"):
        shelf_books = check(shelf_books, command)

print(", ".join(shelf_books))