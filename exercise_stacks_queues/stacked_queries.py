lines = int(input())
stack = []
dic = {
    1: lambda x: stack.append(x[1]),
    2: lambda x: stack.pop() if len(stack) > 0 else None,
    3: lambda x: print(max(stack)) if len(stack) > 0 else None,
    4: lambda x: print(min(stack)) if len(stack) > 0 else None
}

for _ in range(lines):
    number_data = [int(x) for x in input().split()]
    dic[number_data[0]](number_data)

stack.reverse()
print(*stack, sep=", ")