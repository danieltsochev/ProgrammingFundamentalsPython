def function(function_list, function_target):
    for i in range(len(function_list)):
        if -1 < function_list[i] > function_target:
            function_list[i] -= function_target
        elif -1 < function_list[i] <= function_target:
            function_list[i] += function_target
    return function_list


shot_targets = [int(target) for target in input().split()]

last_target = 0
count_of_shot_targets = 0

while True:
    command = input()
    if command == "End":
        break

    current_index = int(command)
    if current_index < 0 or current_index >= len(shot_targets):
        continue

    if shot_targets[current_index] > -1:
        last_target = shot_targets[current_index]
        shot_targets[current_index] = -1
        count_of_shot_targets += 1
        shot_targets = function(shot_targets, last_target)

text = ""
for number in shot_targets:
    text += " "
    text += str(number)


print(f"Shot targets: {count_of_shot_targets} ->{text}")