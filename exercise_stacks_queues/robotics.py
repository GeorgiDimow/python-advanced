from collections import deque
from datetime import datetime, timedelta

robots = {r.split("-")[0]: [int(r.split("-")[1]), 0] for r in input().split(";")} # {name: [time_needed, time_for_curr_task]}

factory_time = datetime.strptime(input(), "%H:%M:%S")
products = deque()

while True:
    product = input()

    if product == "End":
        break

    products.append(product)

while products:
    factory_time += timedelta(0, 1)
    product = products.popleft()

    free_robots = []
    for name, val in robots.items():
        if val[1] != 0:
            robots[name][1] -= 1

    for name, val in robots.items():
        if val[1] == 0:
            free_robots.append([name, val])

    if not free_robots:
        products.append(product)
        continue

    free_name, free_val = free_robots[0]
    robots[free_name][1] = robots[free_name][0]

    print(f"{free_name} - {product} [{factory_time.strftime('%H:%M:%S')}]")

