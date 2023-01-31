def sorting_cheeses(**kwargs):
    sorted_dict = sorted(kwargs.items(), key=lambda n: (-len(n[1]), n[0]))

    result = []

    for cheese, quantity in sorted_dict:
        result.append(cheese)
        result.extend(sorted(quantity, reverse=True))

    return '\n'.join([str(el) for el in result])
