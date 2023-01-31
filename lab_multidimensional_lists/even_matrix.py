rows = int(input())
matrix = []

for _ in range(rows):
    curr_row = [int(element) for element in input().split(', ') if int(element) % 2 == 0]
    matrix.append(curr_row)

print(matrix)