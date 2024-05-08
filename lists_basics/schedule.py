schedule_list = []

def add_task(task):
    schedule_list.append(task)
    print("Task added successfully.")

def remove_task(task):
    if task in schedule_list:
        schedule_list.remove(task)
        print("Task removed successfully.")
    else:
        print("Task not founded in the list.")

def view_task():
    if schedule_list:
        print("Tasks:")
        for task in schedule_list:
            print(task)
    else:
        print("No tasks in the Schedule.")

while True:
    print("\n***Schedule App***")
    print("1: Add task")
    print("2: Remove task")
    print("3: View task")
    print("4: Exit")

    choice = input("Enter an option-> 1, 2, 3 or 4: ")

    if choice == "1":
        task = input("Enter task: ")
        add_task(task)

    elif choice == "2":
        task = input("Enter task to remove: ")
        remove_task(task)

    elif choice == "3":
        view_task()

    elif choice == "4":
        print("Exiting the program!")
        break
    else:
        print("Invalid operation. Please try again!")