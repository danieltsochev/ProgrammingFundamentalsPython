def proces_todo_notes():
    to_do_list = []

    while True:
        notes = input()
        if notes == "End":
            break

        to_do_list.append(notes)
    sorted_notes = sorted(to_do_list, key=lambda x: int(x.split("-")[0]))
    result_sorted_notes = [note.split("-")[1] for note in sorted_notes]
    return result_sorted_notes


print(proces_todo_notes())