from collections import deque


textiles = deque([int(x) for x in input().split(" ")])
medicaments = deque([int(x) for x in input().split(" ")])

healing_items = {
    "Patch": 30,
    "Bandage": 40,
    "MedKit": 100,
}

healing_items_count = {
    "Bandage": 0,
    "MedKit": 0,
    "Patch": 0,
}


while textiles and medicaments:
    curr_textile = textiles.popleft()
    curr_medicaments = medicaments.pop()
    sum_med = curr_textile + curr_medicaments

    if sum_med in healing_items.values():
        if sum_med == healing_items["Patch"]:
            healing_items_count["Patch"] += 1
        if sum_med == healing_items["Bandage"]:
            healing_items_count["Bandage"] += 1
        if sum_med == healing_items["MedKit"]:
            healing_items_count["MedKit"] += 1

        continue
    elif sum_med > healing_items["MedKit"]:
        healing_items_count["MedKit"] += 1
        medicaments[-1] += sum_med - healing_items["MedKit"]
        continue
    else:
        medicaments.append(curr_medicaments + 10)


if not textiles and medicaments:
    print("Textiles are empty.")

if not medicaments and textiles:
    print("Medicaments are empty.")

if not medicaments and not textiles:
    print("Textiles and medicaments are both empty.")

sort_items = sorted(healing_items_count.items(), key=lambda x: x[1], reverse=True)

[print(f"{name} - {count}", sep="\n") for name, count in sort_items if count > 0]

if textiles:
    print(f"Textiles left: {', '.join(str(x) for x in textiles) }")

medicaments.reverse()
if medicaments:
    print(f"Medicaments left: {', '.join(str(x) for x in medicaments) }")