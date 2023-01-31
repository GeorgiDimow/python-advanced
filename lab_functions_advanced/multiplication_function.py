def multiply(*args):
    product = 1
    for num in args:
        product *= num
    return product


# from functools import reduce
# def multiply(*args):
#   return reduce(lambda x, y: x * y, args)