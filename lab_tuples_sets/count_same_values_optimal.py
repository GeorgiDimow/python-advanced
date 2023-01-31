vals = tuple(map(float, input().split()))
counter_of_vals = {}

for val in vals:
    if val not in counter_of_vals:
        counter_of_vals[val] = 0
    counter_of_vals[val] += 1

for k, v in counter_of_vals.items():
     print(f'{k} - {v} times')