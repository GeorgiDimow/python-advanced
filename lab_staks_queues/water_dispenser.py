from collections import deque

quantity = int(input())
names = deque()

COMMAND_END = "End"
COMMAND_START = "Start"
while True:
    command = input()
    if command == COMMAND_START:
        break
    names.append(command)

while True:
    command = list(input().split())
    if command[0] == COMMAND_END:
        break
    elif len(command) == 1:
        if int(command[0]) <= quantity:
            print(f"{names[0]} got water" )
            quantity -= int(command[0])
        else:
            print(f"{names[0]} must wait")
        names.popleft()
    elif len(command) == 2:
        quantity += int(command[1])


print(f"{quantity} liters left")