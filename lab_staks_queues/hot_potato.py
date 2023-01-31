from collections import deque

kids_queue = deque(input().split())
toss = int(input())

while len(kids_queue) > 1:
    for _ in range(toss - 1):
        kids_queue.append(kids_queue.popleft())

    print(f'Removed {kids_queue.popleft()}')

print(f'Last is {kids_queue.pop()}')