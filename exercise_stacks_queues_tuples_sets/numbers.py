set_1 = set([int(x) for x in input().split()])
set_2 = set([int(x) for x in input().split()])

lines = int(input())

dic = {
    "Add First": lambda x: [set_1.add(el) for el in x],
    "Remove First": lambda x: set_1.difference_update({el for el in x}) if len(set_1) > 0 else None,
    "Add Second": lambda x: [set_2.add(el) for el in x],
    "Remove Second": lambda x: set_2.difference_update({el for el in x})  if len(set_2) > 0 else None,
    "Check Subset": lambda x: print(set_1.issubset(set_2) or set_1.issuperset(set_2))
}

for _ in range(lines):
    commands = input().split()
    command = commands.pop(0) + ' ' + commands.pop(0)
    dic[command](list(map(int, commands)))

print(*sorted(set_1), sep=', ')
print(*sorted(set_2), sep=', ')
