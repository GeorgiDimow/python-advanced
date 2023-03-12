row, col = map(int, input().split())

curr_position = []

obstacles_positions = []

opponents_positions = []

field = [[x for x in input().split()] for _ in range(row)]

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}

for r in range(row):
    for c in range(col):
        if field[r][c] == "B":
            curr_position = [r, c]
            field[r][c] = "-"
        elif field[r][c] == "P":
            opponents_positions.append([r, c])
        elif field[r][c] == "O":
            obstacles_positions.append([r, c])

command = input()
touched = 0
moves = 0

while command != "Finish" and touched < 3:
    curr_position[0] += directions[command][0]
    curr_position[1] += directions[command][1]

    if curr_position in obstacles_positions:
        curr_position[0] -= directions[command][0]
        curr_position[1] -= directions[command][1]
        command = input()
        continue

    elif curr_position in opponents_positions:
        touched += 1
        opponents_positions.remove(curr_position)

    elif not (0 <= curr_position[0] < row and 0 <= curr_position[1] < col):
        curr_position[0] -= directions[command][0]
        curr_position[1] -= directions[command][1]
        command = input()
        continue

    moves += 1
    command = input()

print("Game over!")
print(f"Touched opponents: {touched} Moves made: {moves}")