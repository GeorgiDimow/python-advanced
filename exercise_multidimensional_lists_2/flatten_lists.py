matrix = [x.split() for x in input().split("|")]

print(*[' '.join(string) for string in matrix[::-1] if string])