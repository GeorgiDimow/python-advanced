size = int(input())
matrix = [[int(col) for col in input().split()] for row in range(size)]

primary_diagonal = []
secondary_diagonal = []

for i in range(size):
    primary_diagonal.append(matrix[i][i])
    secondary_diagonal.append(matrix[i][-1-i])

print(abs(sum(primary_diagonal) - sum(secondary_diagonal)))