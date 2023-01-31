from collections import deque

bees = deque([int(x) for x in input().split()])
nectar = [int(x) for x in input().split()]
symbols = deque(input().split())

dic_func = {
    "+": lambda x, y: x+y,
    "-": lambda x, y: x-y,
    "*": lambda x, y: x*y,
    "/": lambda x, y: x/y
}

collected = 0

while bees and nectar:
    bee = bees.popleft()
    nec = nectar.pop()
    if bee > nec:
        bees.appendleft(bee)
    elif nec > bee:
        collected += abs(dic_func[symbols.popleft()](bee, nec))


print(f"Total honey made: {collected}")

if bees:
    print(f"Bees left: {', '.join(str(b) for b in bees)}")

if nectar:
    print(f"Nectar left: {', '.join(str(n) for n in nectar)}")