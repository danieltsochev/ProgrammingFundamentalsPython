import re

pattern = r"^[a-zA-Z0-9!@#$?]+=[0-9]+<<.*$"

name_of_mountain = []
coordinates = ""
while True:
    message = input()
    if message == "Last note":
        break
    matches = re.findall(pattern, message)



    if matches:
        for element in matches:
            if element.isalpha():
                name_of_mountain.append(element)
        for element in matches:
            element1 = element.split("<<")

        print(f"Coordinates found {''.join(name_of_mountain)}->{element1[1]}")

    else:
        print("Nothing found!")




