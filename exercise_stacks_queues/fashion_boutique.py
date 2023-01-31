from collections import deque

cloths_stack = deque([int(x) for x in input().split()])
capacity = int(input())
current_capacity = capacity
racks = 1

for _ in cloths_stack.copy():
    if cloths_stack[-1] > current_capacity:
        racks += 1
        current_capacity = capacity
    current_capacity -= cloths_stack.pop()

print(racks)
