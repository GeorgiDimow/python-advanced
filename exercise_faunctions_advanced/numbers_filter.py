def even_odd_filter(**kwargs):
    numbers = kwargs

    if "even" in numbers:
        numbers["even"] = list(filter(lambda x: x % 2 == 0, numbers["even"]))

    if "odd" in numbers:
        numbers["odd"] = list(filter(lambda x: x % 2 != 0, numbers["odd"]))

    return dict(sorted(numbers.items(), key=lambda x: -len(x[1])))


print(even_odd_filter(
    odd=[1, 2, 3, 4, 10, 5],
    even=[3, 4, 5, 7, 10, 2, 5, 5, 2],
))
