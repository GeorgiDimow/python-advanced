from collections import deque

quantity_food = int(input())
orders_queue = deque([int(x) for x in input().split()])

print(max(orders_queue))

for order in orders_queue.copy():
    if order <= quantity_food:
        quantity_food -= order
        orders_queue.popleft()
    else:
        print(f"Orders left: {' '.join([str(o) for o in orders_queue])}")
        break
else:
    print("Orders complete")