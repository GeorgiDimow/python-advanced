expression = input()
indexes = []

for i in range(len(expression)):
    sym = expression[i]

    if sym == '(':
        indexes.append(i)
    elif sym == ')':
        j = indexes.pop()
        print(expression[j:i+1])