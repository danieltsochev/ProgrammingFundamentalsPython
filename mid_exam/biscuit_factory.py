from math import floor

biscuits_per_day_worker = int(input())
workers_count = int(input())
amount_biscuits_month_competing = int(input())
result = 0

for day in range(30):
    if day % 3 == 0:
        result += floor(0.75 * (workers_count * biscuits_per_day_worker))
    else:
        result += floor(workers_count * biscuits_per_day_worker)

percent_difference = abs((result / amount_biscuits_month_competing) * 100 - 100)

print(f"You have produced {result} biscuits for the past month.")

if result > amount_biscuits_month_competing:
    print(f"You produce {percent_difference:.2f} percent more biscuits.")

elif result < amount_biscuits_month_competing:
    print(f"You produce {percent_difference:.2f} percent less biscuits.")