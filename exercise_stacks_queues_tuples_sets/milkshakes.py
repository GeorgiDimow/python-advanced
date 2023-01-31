from collections import deque

chocolates = [int(x) for x in input().split(", ")]
cups_of_milk = deque([int(x) for x in input().split(", ")])
milkshakes = 0

while chocolates and cups_of_milk and milkshakes < 5:
    chocolate = chocolates[-1]
    milk = cups_of_milk[0]
    if chocolate == milk and milk > 0 and chocolate > 0:
        milkshakes += 1
        chocolates.pop()
        cups_of_milk.popleft()
    elif chocolate != milk and milk > 0 and chocolate > 0:
        if chocolate - 5 > 0:
            chocolates[-1] -= 5
        else:
            chocolates.pop()
        cups_of_milk.append(cups_of_milk.popleft())

    if chocolate <= 0:
        chocolates.pop()
    if milk <= 0:
        cups_of_milk.popleft()


empty = "empty"

if milkshakes == 5:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")
print(f"Chocolate: {', '.join([str(c) for c in chocolates] ) if chocolates else empty}")
print(f"Milk: {', '.join([str(c) for c in cups_of_milk] ) if cups_of_milk else empty}")