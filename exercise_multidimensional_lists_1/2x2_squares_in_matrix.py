<<<<<<< HEAD
row, col = [int(x) for x in input().split()]

matrix = [[x for x in input().split()] for _ in range(row)]
count = 0

for r in range(row-1):
    for c in range(col-1):
        index_func = (
            (r+1, c),
            (r+1, c+1),
            (r, c+1)
        )
        curr_pos = matrix[r][c]
        curr_pos_down = matrix[index_func[0][0]][index_func[0][1]]
        curr_pos_diag = matrix[index_func[1][0]][index_func[1][1]]
        curr_pos_right = matrix[index_func[2][0]][index_func[2][1]]

        if curr_pos == curr_pos_down == curr_pos_right == curr_pos_diag:
            count += 1

print(count)
=======
row, col = [int(x) for x in input().split()]

matrix = [[x for x in input().split()] for _ in range(row)]
count = 0

for r in range(row-1):
    for c in range(col-1):
        index_func = (
            (r+1, c),
            (r+1, c+1),
            (r, c+1)
        )
        curr_pos = matrix[r][c]
        curr_pos_down = matrix[index_func[0][0]][index_func[0][1]]
        curr_pos_diag = matrix[index_func[1][0]][index_func[1][1]]
        curr_pos_right = matrix[index_func[2][0]][index_func[2][1]]

        if curr_pos == curr_pos_down == curr_pos_right == curr_pos_diag:
            count += 1

print(count)
>>>>>>> fb6ccd4 (latest work)
