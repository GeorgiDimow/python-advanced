vals = tuple(map(float, input().split()))
counter_of_vals = {val: vals.count(val) for val in vals}

for k, v in counter_of_vals.items():
     print(f'{k} - {v} times')