size = int(input())
matrix = [[int(col) for col in input().split(', ')] for row in range(size)]

primary_diagonal = []
secondary_diagonal = []

for i in range(size):
    primary_diagonal.append(matrix[i][i])
    secondary_diagonal.append(matrix[i][-1-i])

print(f"Primary diagonal: {', '.join(str(x) for x in primary_diagonal)}. Sum: {sum(primary_diagonal)}")
print(f"Secondary diagonal: {', '.join([str(a) for a in secondary_diagonal])}. Sum: {sum(secondary_diagonal)}")