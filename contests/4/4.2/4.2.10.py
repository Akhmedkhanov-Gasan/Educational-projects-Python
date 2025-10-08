def choice(*args, **kwargs):
    f = kwargs.get('max') or kwargs.get('min')
    g = max if 'max' in kwargs else min
    return g(map(f, args))


result = choice(321, 87, 1000, -23, min=lambda x: len(str(x)))
print(result)