rows, colums = map(int, input().split(', '))
matrix = []
for row in range(rows):
    row_data = list(map(int, input().split(', ')))
    matrix.append(row_data)

sum = sum([sum(curr_el) for curr_el in matrix])
print(sum)
print(matrix)