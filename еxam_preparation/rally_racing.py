n = int(input())
racing_number = input()
matrix = [input().split() for i in range(n)]

coord_f = ()
coord_t1 = ()
coord_t2 = ()

for row in range(n):
    for col in range(n):
        if "F" in matrix[row][col]:
            coord_f = [row, col]
        elif "T" in matrix[row][col]:
            if not coord_t1:
                coord_t1 = [row, col]
            else:
                coord_t2 = [row, col]


directions_dict ={
    "left": (0, -1),
    "right": (0, 1),
    "up": (-1, 0),
    "down": (1, 0),
}

command = input()
curr_pos = [0, 0]
dis_covered = 0

while command != "End":
    curr_pos[0] += directions_dict[command][0]
    curr_pos[1] += directions_dict[command][1]
    if curr_pos == coord_t1:
        dis_covered += 30
        matrix[curr_pos[0]][curr_pos[1]] = "."
        curr_pos = coord_t2
        matrix[curr_pos[0]][curr_pos[1]] = "."
        coord_t1 = ()
        coord_t2 = ()

    elif curr_pos == coord_t2:
        dis_covered += 30
        matrix[curr_pos[0]][curr_pos[1]] = "."
        curr_pos = coord_t1
        matrix[curr_pos[0]][curr_pos[1]] = "."
        coord_t1 = ()
        coord_t2 = ()

    elif curr_pos == coord_f:
        curr_pos = coord_f
        matrix[curr_pos[0]][curr_pos[1]] = "C"
        print(f"Racing car {racing_number} finished the stage!")
        dis_covered += 10
        break

    elif matrix[curr_pos[0]][curr_pos[1]] == '.':
        dis_covered += 10

    command = input()
else:
    print(f"Racing car {racing_number} DNF.")


print(f"Distance covered {dis_covered} km.")
matrix[curr_pos[0]][curr_pos[1]] = "C"
[print(''.join(row)) for row in matrix]