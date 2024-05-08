def cheer_calculation(function_office_rooms):
    total_chairs_left = 0
    chairs_needed = 0
    room_number = 0

    for iteration in range(function_office_rooms):
        current_room = [room for room in input().split()]
        room_number += 1
        chairs = current_room[0]
        people = int(current_room[1])
        if len(chairs) < people:
            chairs_needed = people - len(chairs)
            print(f"{chairs_needed} more chairs needed in room {room_number}")
        else:
            total_chairs_left += len(chairs) - people
    if chairs_needed <= 0:
        print(f"Game On, {total_chairs_left} free chairs left")


office_rooms = int(input())

cheer_calculation(office_rooms)