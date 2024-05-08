def add(add_list, add_action):
    command = add_action[0]
    card = add_action[1]
    if card not in add_list:
        add_list.append(card)
        print("Card successfully added")
    else:
        print("Card is already in the deck")
    return add_list


def remove(remove_list, remove_action):
    command = remove_action[0]
    card = remove_action[1]
    if card in remove_list:
        remove_list.remove(card)
        print("Card successfully removed")
    else:
        print("Card not found")
    return remove_list


def remove_at(remove_at_list, remove_at_action):
    command = remove_at_action[0]
    index = int(remove_at_action[1])
    if index > len(remove_at_list) or index < 0:
        print("Index out of range")
    else:
        remove_at_list.remove(remove_at_list[index])
        print("Card successfully removed")
    return remove_at_list


def insert(insert_list, insert_action):
    command = insert_action[0]
    index = int(insert_action[1])
    card = insert_action[2]
    if index > len(insert_list) or index < 0:
        print("Index out of range")
    elif insert_list[index] != card:
        insert_list.insert(index, card)
        print("Card successfully added")
    else:
        print("Card is already added")
    return insert_list


deck_of_cards = [card for card in input().split(", ")]
command_count = int(input())

action = ""

for iteration in range(command_count):
    action = [action for action in input().split(", ")]

    if "Add" in action:
        add(deck_of_cards, action)

    elif "Remove" in action:
        remove(deck_of_cards, action)

    elif "Remove At" in action:
        remove_at(deck_of_cards, action)

    elif "Insert" in action:
        insert(deck_of_cards, action)


print(", ".join(deck_of_cards))
