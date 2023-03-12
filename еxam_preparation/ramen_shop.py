from collections import deque

DAYS = 7

bowls_of_ramen = deque([int(x) for x in input().split(", ")])
customers = deque([int(x) for x in input().split(", ")])

while bowls_of_ramen and customers:
    curr_ramen = bowls_of_ramen.pop()
    curr_customer = customers.popleft()

    if curr_ramen > curr_customer:
        bowls_of_ramen.append(curr_ramen - curr_customer)
        continue
    elif curr_ramen < curr_customer:
        customers.appendleft(curr_customer - curr_ramen)
        continue


if not customers:
    print("Great job! You served all the customers.")
    if bowls_of_ramen:
        print(f"Bowls of ramen left: {', '.join(str(x) for x in bowls_of_ramen)}")
else:
    print("Out of ramen! You didn't manage to serve all customers.")
    print(f"Customers left: {', '.join(str(x) for x in customers)}")