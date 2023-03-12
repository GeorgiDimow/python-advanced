def grocery_store(**prods):
    prods = sorted(prods.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))
    result = []
    [result.append(f"{prod}: {quan}") for prod, quan in prods]
    return '\n'.join(result)


print(grocery_store(
    bread=5,
    pasta=12,
    eggs=12,
))
