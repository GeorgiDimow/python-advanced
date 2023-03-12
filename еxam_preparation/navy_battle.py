

size = int(input())

coord_mines = set()
submarine = []
battle_cruisers = set()
matrix = [list(input()) for _ in range(size)]
curr_pos = 0

directions_dict = {
    "left": (0, -1),
    "right": (0, 1),
    "up": (-1, 0),
    "down": (1, 0),
}

for row in range(size):
    for col in range(size):
        curr_pos = matrix[row][col]
        if curr_pos == "S":
            submarine = [row, col]
        elif curr_pos == "*":
            coord_mines.add((row, col))
        elif curr_pos == "C":
            battle_cruisers.add((row, col))

health = 3
command = input()
x = submarine[0]
y = submarine[1]
matrix[x][y] = '-'

while battle_cruisers:
    if health == 0:
        break

    x += directions_dict[command][0]
    y += directions_dict[command][1]
    curr_pos = matrix[x][y]
    matrix[x][y] = '-'
    if curr_pos == "*":
        coord_mines.remove((x, y))
        health -= 1
    elif curr_pos == "C":
        battle_cruisers.remove((x, y))

    command = input()

else:
    print("Mission accomplished, U-9 has destroyed all battle cruisers of the enemy!")


if health == 0:
    print(f"Mission failed, U-9 disappeared! Last known coordinates {[x, y]}!")

matrix[x][y] = 'S'
[print(*row, sep='') for row in matrix]