def product(*args, **kwargs):
    words = list(args)
    result = []
    for word in words:
        number = 0
        for key, value in kwargs.items():
            if key in word:
                if number == 0:
                    number = value
                else:
                    number *= value
        if number == 0:
            continue
        result.append(number)
    return tuple(result)

result = product("Ann", "Bob", "Chuck", a=9, n=5, u=3, c=2, A=5)
print(result)