size = int(input())
matrix = [input().split() for _ in range(size)]

positions = (
    (-1, 0, "up"),  #
    (1, 0, "down"),
    (0, -1, "left"),
    (0, 1, "right"),
)
max_eggs = 0
most_eggs_path_pos = []

paths = {
    "up": [],
    "down": [],
    "left": [],
    "right": []

}

for row in range(size):
    for col in range(size):
        if matrix[row][col] == 'B':
            eggs = 0

            for pos in positions:
                pos_row = row + pos[0]
                pos_col = col + pos[1]
                path = pos[2]
                curr_path = []
                while 0 <= pos_row < size and 0 <= pos_col < size:
                    curr_pos = matrix[pos_row][pos_col]
                    if curr_pos.isdigit():
                        eggs = int(curr_pos)
                    elif curr_pos == 'X':
                        break

                    curr_path.append([pos_row, pos_col])
                    max_eggs += eggs
                    pos_row += pos[0]
                    pos_col += pos[1]

                paths[path].append(max_eggs)
                paths[path].append(curr_path)
                max_eggs = 0

longest_path = ''
for path in paths.items():
    if max_eggs <= path[1][0]:
        max_eggs = path[1][0]
        most_eggs_path_pos = path[1][1]
        longest_path = path[0]

print(longest_path)
print(*most_eggs_path_pos, sep="\n")
print(max_eggs)
