n = int(input())
items = [input().split() for _ in range(n)]
students_data = {name: [].append(grade) for name, grade in items}

print(students_data)