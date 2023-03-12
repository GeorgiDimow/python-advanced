row, col = [int(x) for x in input().split()]

matrix = [[x for x in input().split() ] for _ in range(row)]

command = input()

while command != "END":
    if not len(command.split()) == 5:
        print("Invalid input!")
        command = input()
        continue

    swap = command.split()[0]
    x1 = int(command.split()[1])
    y1 = int(command.split()[2])
    x2 = int(command.split()[3])
    y2 = int(command.split()[4])

    if swap == "swap" and 0 <= x1 <= row and 0 <= y1 <= col and 0 <= x2 <= row and 0 <= y2 <= col:
        matrix[x1][y1], matrix[x2][y2] = matrix[x2][y2], matrix[x1][y1]
        [print(*r) for r in matrix]
    else:
        print("Invalid input!")

    command = input()

