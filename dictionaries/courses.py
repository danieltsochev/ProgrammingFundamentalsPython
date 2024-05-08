courses = {}

while True:

    information = input()

    if information == "end":
        break

    course, username = information.split(":")

    if course not in courses:
        courses[course] = []
    courses[course].append(username)


for course, username in courses.items():
    print(f"{course}: {len(username)}")

    for current_user in username:
        print(f"--{current_user}")
