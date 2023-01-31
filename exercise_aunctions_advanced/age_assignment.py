def age_assignment(*args, **kwargs):
    result = []

    for letter, age in kwargs.items():
        person_name = list(filter(lambda x: x.startswith(letter), args))[0]

        result.append(f"{person_name} is {age} years old.")

    return '\n'.join(sorted(result))


print(age_assignment("Peter", "George", G=26, P=19))