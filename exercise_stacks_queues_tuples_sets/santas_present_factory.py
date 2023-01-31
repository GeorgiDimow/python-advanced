from collections import deque

materials = [int(x) for x in input().split()]
magic_levels = deque([int(x) for x in input().split()])

presents = {
    150: [0, "Doll"],
    250: [0, "Wooden train"],
    300: [0, "Teddy bear"],
    400: [0, "Bicycle"],
}

while materials and magic_levels:
    curr_box = materials.pop() if magic_levels[0] or not materials[0] else 0
    curr_level = magic_levels.popleft() if curr_box or not magic_levels[0] else 0

    if not curr_level:
        continue

    product = curr_box * curr_level

    if product == 150 or product == 250 or product == 300 or product == 400:
        presents[product][0] += 1
    elif product < 0:
        materials.append(curr_box + curr_level)
    elif product > 0:
        materials.append(curr_box + 15)

pair_1 = presents[150][0] > 0 and presents[250][0] > 0
pair_2 = presents[300][0] > 0 and presents[400][0] > 0

materials.reverse()

if pair_1 or pair_2:
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")
if materials:
    print(f"Materials left: {', '.join(str(x) for x in materials)}")
if magic_levels:
    print(f"Magic left: {', '.join(str(x) for x in magic_levels)}")

if presents[400][0] > 0:
    print(f"{presents[400][1]}: {presents[400][0]}")
if presents[150][0] > 0:
    print(f"{presents[150][1]}: {presents[150][0]}")
if presents[300][0] > 0:
    print(f"{presents[300][1]}: {presents[300][0]}")
if presents[250][0] > 0:
    print(f"{presents[250][1]}: {presents[250][0]}")
