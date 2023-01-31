from collections import deque

queue = deque()
COMMAND_END = "End"
COMMAND_PAID = "Paid"

while True:
    command = input()
    if command == COMMAND_PAID:
        while queue:
            print(queue.popleft())
    elif command == COMMAND_END:
        print(f"{len(queue)} people remaining.")
        break
    else:
        queue.append(command)