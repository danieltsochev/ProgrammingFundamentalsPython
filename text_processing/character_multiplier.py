def same_length(inside_list):
    total_sum = 0
    first = inside_list[0]
    second = inside_list[1]

    for index in range(0, len(first)):
        total_sum += (ord(first[index]) * ord(second[index]))
    return total_sum


def different_length(inside_list):
    long = ""
    short = ""
    extra_elements = []
    total_sum = 0

    if len(inside_list[0]) < len(inside_list[1]):
        long = inside_list[1]
        short = inside_list[0]
    elif len(inside_list[0]) > len(inside_list[1]):
        long = inside_list[0]
        short = inside_list[1]

    for index, element in enumerate(long):
        if index >= len(short):
            extra_elements.append(element)
            long = long[:len(short)]

    for index in range(0, len(long)):
        total_sum += (ord(long[index]) * ord(short[index]))

    for element in extra_elements:
        total_sum += ord(element)
    return total_sum


two_strings = input().split()
result = 0

if len(two_strings[0]) == len(two_strings[1]):
    result = same_length(two_strings)
else:
    result = different_length(two_strings)

print(result)