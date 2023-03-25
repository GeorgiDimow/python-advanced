def type_check(type_data):
    def decorator(func):
        def wrapper(*args):
            for arg in args:
                if not isinstance(arg, type_data):
                    return "Bad Type"

            return func(*args)

        return wrapper

    return decorator


@type_check(int)
def times2(num):
    return num*2

print(times2(2))
print(times2('Not A Number'))
