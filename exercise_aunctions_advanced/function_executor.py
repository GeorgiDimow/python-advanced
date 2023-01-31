def func_executor(*func_data):
    return '\n'.join([f"{func.__name__} - {func(*args)}" for func, args in func_data])