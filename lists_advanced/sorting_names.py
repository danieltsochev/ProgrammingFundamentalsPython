def sorting_names():
    list_of_names = input().split(", ")
    sorted_names = sorted(list_of_names, key=lambda x: (-len(x), x))
    return sorted_names


result = sorting_names()
print(result)