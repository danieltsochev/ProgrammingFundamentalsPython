def greater_average(function_list):
    greater_list = [number for number in function_list if number > average]
    if len(greater_list) <= 0:
        print("No")
    return greater_list


def sorting_greater_numbers(function_list2):
    sorted_greater_list = sorted(function_list2, reverse=True)
    final_sorting_list = []
    for number in sorted_greater_list:
        if number > average:
            final_sorting_list.append(number)
        if len(final_sorting_list) >= 5:
            break

    return final_sorting_list


numbers_list = [int(number) for number in input().split()]
average = sum(numbers_list) / len(numbers_list)

result = sorting_greater_numbers(greater_average(numbers_list))
print(*result)