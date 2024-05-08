def time_calculation(average, students):
    hour_counter = 0
    people_served = 0

    while True:
        if people_served >= students:
            break
        hour_counter += 1
        if hour_counter % 4 == 0:
            continue
        else:
            people_served += average
    return f"Time needed: {hour_counter}h."


first_employee_efficiency = int(input())
second_employee_efficiency = int(input())
third_employee_efficiency = int(input())
students_count = int(input())

average_efficiency = first_employee_efficiency + second_employee_efficiency + third_employee_efficiency
print(time_calculation(average_efficiency, students_count))