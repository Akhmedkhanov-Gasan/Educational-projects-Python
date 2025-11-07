def make_equation(*args):
    if len(args) == 1:
        return args[0]
    inner = make_equation(*args[:-1])
    return f'({inner}) * x + {args[-1]}'


result = make_equation(3, 2, 1)
print(result)