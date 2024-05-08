def character_in_range(element1, element2):
    for character in range(ord(element1) + 1, ord(element2)):

        new_element = chr(character)
        print(new_element, end=" ")


first_character = input()
second_character = input()

character_in_range(first_character, second_character)